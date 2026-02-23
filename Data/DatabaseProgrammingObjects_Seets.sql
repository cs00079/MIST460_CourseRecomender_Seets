use MIST460_RDB_Seets

GO

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
join Course C on S.CourseID = C.CourseID
join Instructor I on S.InstructorID = I.InstructorID
where S.SectionSemester = N'Spring'
and S.SectionYear = 2026
and C.SubjectCode = 'MIST'
and C.CourseNumber = '460'
