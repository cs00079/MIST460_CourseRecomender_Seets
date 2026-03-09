use MIST460_RDB_Seets

GO
--what are the sections of a specific course offered this semester spring 2026
Declare @semester NVARCHAR(20) = N'Spring'
Declare @year INT = 2026
Declare @subjectCode NVARCHAR(10) = 'MIST'
Declare @courseNumber NVARCHAR(10) = '460'

select
    C.SubjectCode, 
    C.CourseNumber, 
    C.Title, 
    S.SectionID, 
    S.CRN, 
    S.SectionNumber, 
    S.SectionSemester, 
    S.SectionYear, 
    S.RemainingOpenings,
    I.FirstName + ' ' + I.LastName AS InstructorName
from Section S  
inner join Course C on S.CourseID = C.CourseID
inner join Instructor I on S.InstructorID = I.InstructorID
where S.SectionSemester = N'Spring'
and S.SectionYear = 2026
and C.SubjectCode = 'MIST'
and C.CourseNumber = '460'

--what are the prerequisites for a specific course(optional entry)
declare @subjectCode NVARCHAR(10) = 'MIST'
declare @courseNumber NVARCHAR(10) = '460'

select
    C.SubjectCode + ' ' + C.CourseNumber AS Course,
    P.SubjectCode + ' ' + P.CourseNumber AS Prerequisite,
    CP.MinGradeRequired
from CoursePrerequisite CP
inner join Course C on CP.CourseID = C.CourseID
inner join Course P on CP.PrerequisiteID = P.CourseID
where C.SubjectCode = 'MIST'
and C.CourseNumber = '460'

--Has specific student completed the prerequisites for a specific course a specific course





