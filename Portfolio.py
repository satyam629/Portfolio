import streamlit as st

# Set up the page layout and title
st.set_page_config(page_title="Satyam - Data Engineer Portfolio", layout="wide")

# Custom Fonts
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    body {
        font-family: 'Roboto', sans-serif;
    }
    .header {
        text-align: center;
        padding: 40px 0;
        background-color: #343a40;
        color: white;
        border-bottom: 4px solid #007bff;
    }
    nav {
        display: flex;
        justify-content: center;
        background-color: rgba(255, 255, 255, 0.9);
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    nav a {
        margin: 0 15px;
        color: #007bff;
        text-decoration: none;
        font-weight: bold;
    }
    .section {
        padding: 20px;
        margin: 20px 0;
        background: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .skill {
        margin: 10px 0;
    }
    .contact-form input, .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    .contact-form button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: white;
        cursor: pointer;
    }
    .contact-form button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown("<div class='header'><h1>Satyam</h1><h2>Senior Data Engineer</h2><p>Bengaluru, India · +91 9031294999 · satyam121satyam121@gmail.com</p></div>", unsafe_allow_html=True)

# Navigation
st.markdown("""
<nav>
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.header("Transforming Data with AWS, Snowflake & PySpark")
st.image("https://your-hero-image-url.com", use_column_width=True)  # Add a hero image URL

# About Section
st.markdown("<div class='section' id='about'><h3>About Me</h3><p>I am a Senior Data Engineer with 3+ years of experience, specializing in transitioning legacy data warehouses to Snowflake on AWS. My expertise includes AWS Glue, Snowpark, PySpark, and SQL, focusing on optimizing ETL pipelines for large-scale analytics.</p></div>", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section' id='skills'><h3>Skills</h3>", unsafe_allow_html=True)
skills = {
    "AWS Glue, S3, Redshift": "Building data pipelines, storing and transforming data.",
    "Snowflake": "Data warehousing, Snowpark, advanced SQL for data processing.",
    "PySpark": "Efficient processing of big data using partitioning, bucketing, and transformations.",
    "SQL": "Strong command in SQL including pivoting, stored procedures, and optimizing data transformations."
}

for skill, description in skills.items():
    st.markdown(f"<div class='skill'><strong>{skill}</strong><br>{description}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Projects Section with Carousel
st.markdown("<div class='section' id='projects'><h3>Key Projects</h3>", unsafe_allow_html=True)
projects = [
    {
        "title": "Data Warehousing for BASF",
        "description": "Optimized Snowflake data warehousing solutions, transforming large datasets using AWS Glue, achieving a 40% improvement in processing time.",
        "image": "https://your-project-image-url.com"  # Replace with project image URL
    },
    {
        "title": "Cloud Migration for Pharmaceutical KPIs",
        "description": "Led the migration of legacy data warehouses to Snowflake on AWS, ensuring minimal downtime and increased scalability.",
        "image": "https://your-project-image-url.com"  # Replace with project image URL
    },
]

for project in projects:
    st.image(project["image"], width=300)  # Project image
    st.markdown(f"<strong>{project['title']}</strong><br>{project['description']}<br><br>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
st.markdown("<div class='section' id='contact'><h3>Contact Me</h3><form class='contact-form'>Send me a message:<br><input type='text' placeholder='Your Name' required><br><input type='email' placeholder='Your Email' required><br><textarea placeholder='Your Message' required></textarea><br><button type='submit'>Send Message</button></form></div>", unsafe_allow_html=True)

# Add LinkedIn and Email links
st.markdown("""
### Or reach me on:
- [LinkedIn](https://www.linkedin.com/in/satyam-51a740102/)
- Email: satyam121satyam121@gmail.com
""")

# Footer
st.markdown("<div style='text-align:center; padding: 20px;'><p>&copy; 2024 Satyam - Senior Data Engineer</p></div>", unsafe_allow_html=True)
