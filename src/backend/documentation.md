# API Documentation

Ill make this more in-depth later

## Main Syllabi Initialization

Access the main syllabi processing via the '/process' route.

Send raw syllabus text as a JSON object with the singular field 'raw_syllabus'.

    {
        'raw_syllabus': "Syllabus text here..."
    }


You will receive a JSON object in return shaped like:

    {
        "status": "valid",
        "course_id": "528491",
        "course_name": "Underwater Basket Weaving",
        "course_dates": "{'start_date': '2026-01-05', 'end_date': '2026-03-30'}",
        "instructor": "Gandalf the Grey",
        "processing_date": "2026-02-11",
        "raw_text": {
            "raw_syllabus": "When Mr Bilbo Baggins of Bag End announced that he would shortly be celebrating his eleventy-first birthday with a party of special magnificence, there was much talk and excitement in Hobbiton."
        },
        "sections": {
            "late_policy": "The late_policy is...",
            "prerequisites": "The prerequisites are...",
            "course_info": "The course_info is...",
            "materials": "The materials are...",
            "course_content": "The course_content is...",
            "grading_scale": "The grading_scale is...",
            "grading_categories": "The grading_categories are...",
            "assignments": "The assignments are...",
            "lab_info": "The lab_info is...",
            "exam_policy": "The exam_policy is...",
            "support_info": "The support_info is...",
            "accommodations": "The accommodations are...",
            "academic_integrity": "The academic_integrity policy is...",
            "ai_policy": "The ai_policy is...",
            "wellness_resources": "The wellness_resources are...",
            "student_rights": "The student_rights are..."
        }
    }
This example contains placeholder values for the fields. Expect the sections on the first level 
of the JSON object ("course_id" through "processing_date") to contain basic values representing their category.
The elements contained in the "sections" level will however contain user-ready explanations for each topic.


The /process route also verifies the authenticity of the syllabus. If it user's data does not appear to by
an actual syllabus from a class, it will return a JSON object with the class_id value of "INVALID":
    
    {
        "class_id": "invalid"
    }

If the data that is returned has the "class_id" "INVALID", then display a message to the user that the syllabus is invalid.

If the raw data received by the /process route is in itself invalid (ie an issue in the transmission, bad formatting), it will
return a JSON object with the "status" of "error":

    {
        "status": "error"
    }