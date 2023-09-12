from fastapi import APIRouter, status

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
def read_cv():
    return {
        "about_me": {
            "intro": (
                "Hello, I'm Aldo, a Software Engineer with a focus on "
                "Python development. I have expertise in Docker, AWS "
                "services, Linux, server maintenance, and SQL."
            )
        },
        "skills": {
            "python": (
                "My primary programming language for developing scalable "
                "and robust applications."
            ),
            "docker": (
                "Expertise in containerizing applications for consistent "
                "development and deployment."
            ),
            "aws_services": (
                "Proficient in leveraging various AWS services for "
                "cloud-based solutions."
            ),
            "linux_server_maintenance": (
                "Skilled in Linux administration and maintaining servers "
                "for optimal performance."
            ),
            "sql": (
                "Adept at designing and managing databases, ensuring quick "
                "and secure data access."
            ),
        },
        "projects": (
            "Here you'll find a variety of projects that I've worked on, "
            "demonstrating my skills in Python development, cloud services, and more."
        ),
        "contact": (
            "Feel free to reach out if you're interested in collaborating "
            "or have any questions. email: aldomatusmartinez@gmail.com"
        ),
    }
