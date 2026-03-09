use MIST460_RDB_Seets
GO

--Need days / times for sections, location

-- Database Programming Objects (Stored Procedures, User-Defined Functions UDF -> Scalar, Table-valued, Triggers)

--1. what are the sections of a specific course offered this semester spring 2026

-- Inputs: SubjectCode and CourseNumber (Course)
--Conditions: Offered in Spring 2026 (Section)
--Output: SectionID, Instructor Name, Remaining Openings (Section + Instructor)

Create or alter procedure GetCourseSectionsForSpecifiedCourse
(
    @subjectCode NVARCHAR(10),
    @courseNumber NVARCHAR(10)
)
AS
BEGIN
    select
        C.SubjectCode,
        C.CourseNumber,
        C.Title,
        S.SectionID,
        S.CRN,
        S.SectionNumber,
        S.SectionSemester,
        S.SectionYear,
        S.RemainingOpenings
        I.FirstName + ' ' + I.LastName AS InstructorName
    from Section S
        join Course C on S.CourseID = C.CourseID
        join Instructor I on S.InstructorID = I.InstructorID
    where S.SectionSemester = dbo.GetSemesterFromMonth()
    and S.SectionYear = YEAR(GETDATE())
    and C.SubjectCode = ISNULL(@subjectCode, C.SubjectCode
    and C.CourseNumber = ISNULL(@courseNumber, C.CourseNumber)

End;

/*
execute GetCourseSectionsForSpecifiedCourse
    @subjectCode = 'MIST',
    @courseNumber = '460'
*/

GO

--scalar function to get a semester base on month number

create or alter function dbo.fnGetSemesterFromMonth
returns nvarchar(20)
AS
BEGIN
    Declare @monthNumber int = MONTH(GETDATE());
    declare @semester nvarchar(20);

    if @MonthNumber in (1, 2, 3, 4, 5)
        set @semester = N'Spring';
    else if @MonthNumber in (6, 7)
        set @semester = N'Summer';
    else
        set @semester = N'Fall';
    
    return @semester;
END;

-- select dbo.GetSemesterFromMonth() as CurrentSemester;


-- 2. what are the prerequisites for a specific course(optional entry)
GO

declare @subjectCode NVARCHAR(10);
declare @courseNumber NVARCHAR(10);

set @subjectCode = 'MIST';
set @courseNumber = '460';

select
    C.SubjectCode + ' ' + C.CourseNumber AS Course,
    P.SubjectCode + ' ' + P.CourseNumber AS Prerequisite,
    CP.MinGradeRequired
from CoursePrerequisite CP
inner join Course C on CP.CourseID = C.CourseID
inner join Course P on CP.PrerequisiteID = P.CourseID
where C.SubjectCode = @SubjectCode 
and C.CourseNumber = @CourseNumber;



-- 3. Has specific student completed the prerequisites for a specific course a specific course

-- Find all the courses that specified student has completed

GO

create or alter function fnGetStudentCourseHistory
(
    @studentID INT
)
returns @CourseHistory TABLE
(
    SubjectCode NVARCHAR(10),
    CourseNumber NVARCHAR(10),
    Grade CHAR(2)
)
AS
BEGIN
    INSERT INTO @CourseHistory 
    (SubjectCode, CourseNumber, Grade)
    SELECT 
        C.SubjectCode, 
        C.CourseNumber, 
        rs.LetterGrade
    FROM Registration R
        join RegistrationSection RS on R.RegistrationID = RS.RegistrationID
        join Section S on RS.SectionID = S.SectionID
        join Course C on S.CourseID = C.CourseID
    where R.StudentID = @studentID

    return;
END


-- select * from fnGetStudentCourseHistory(1);

GO

create or alter function fnGradePointsFromLetterGrade
(
    @letterGrade CHAR(2)
)
returns INT
AS
BEGIN  
    declare @gradePoints INT;

    set @GradePoints = case @LetterGrade
        when 'A' then 4
        when 'B' then 3
        when 'C' then 2
        when 'D' then 1
        when 'F' then 0
        else 0 
    end;

    return @GradePoints;
end;

select * from fnGetCrousePrerequisites('MIST', '460') as Prerequisites
join fnGetStudentCourseHistory(1) as CourseHistory
on Prerequisites.SubjectCode = CourseHistory.SubjectCode
and Prerequisites.CourseNumber = CourseHistory.CourseNumber


--Trigger -> automatic execution in response to certain events (e.g., insert, update, delete) on a table.
-- Enroll a student in a section (insert into RegistrationSection)
--create procedure procEnrollStudentInSection(@studentID int, @sectionID int)

GO 

create TRIGGER trgDecreaseSectionSeats
ON RegistrationSection
after insert -- triggering event
AS
BEGIN
    update S
    Set remainingOpenings = remainingOpenings - 1
    from Section S
    join inserted I on S.SectionID = I.SectionID
END





