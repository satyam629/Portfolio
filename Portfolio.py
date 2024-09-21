import streamlit as st

# Set up the page layout and title
st.set_page_config(page_title="Satyam - Data Engineer Portfolio", layout="wide")

# Image URLs
aws_logo_url = "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg"
snowflake_logo_url = "https://upload.wikimedia.org/wikipedia/commons/f/ff/Snowflake_Logo.svg"
pyspark_logo_url = "https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg"

# Background Style
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f8f9fa;
    }
    .header {
        text-align: center;
        padding: 40px 0;
        background-color: #343a40;
        color: white;
    }
    h1, h2, h3 {
        margin: 0;
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
        color: #343a40;
        text-decoration: none;
        font-weight: bold;
    }
    nav a:hover {
        text-decoration: underline;
    }
    .section {
        padding: 20px;
        margin: 20px 0;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
    <a href="#about">About</a> | 
    <a href="#skills">Skills</a> | 
    <a href="#projects">Projects</a> | 
    <a href="#contact">Contact</a>
</nav>
""", unsafe_allow_html=True)

# Hero Section with Logos
st.header("Transforming Data with AWS, Snowflake & PySpark")
col1, col2, col3 = st.columns(3)

with col1:
    st.image(aws_logo_url, caption="AWS", width=150)
with col2:
    st.image(snowflake_logo_url, caption="Snowflake", width=150)
with col3:
    st.image(pyspark_logo_url, caption="PySpark", width=150)

# About Section
st.markdown("<div class='section' id='about'><h3>About Me</h3><p>I am a Senior Data Engineer with 3+ years of experience, specializing in transitioning legacy data warehouses to Snowflake on AWS. I have expertise in AWS Glue, Snowpark, PySpark, and SQL, focusing on optimizing ETL pipelines for large-scale analytics.</p></div>", unsafe_allow_html=True)

# Skills Section
st.markdown("<div class='section' id='skills'><h3>Skills</h3><ul><li>AWS Glue, S3, Redshift: Building data pipelines, storing and transforming data.</li><li>Snowflake: Data warehousing, Snowpark, advanced SQL for data processing.</li><li>PySpark: Efficient processing of big data using partitioning, bucketing, and transformations.</li><li>SQL: Strong command in SQL including pivoting, stored procedures, and optimizing data transformations.</li></ul></div>", unsafe_allow_html=True)

# Projects Section
st.markdown("<div class='section' id='projects'><h3>Key Projects</h3><ul><li><strong>Data Warehousing for BASF:</strong> Optimized Snowflake data warehousing solutions, transforming large datasets using AWS Glue, achieving a 40% improvement in processing time.</li><li><strong>Cloud Migration for Pharmaceutical KPIs:</strong> Led the migration of legacy data warehouses to Snowflake on AWS, ensuring minimal downtime and increased scalability.</li></ul></div>", unsafe_allow_html=True)

# Contact Section
st.markdown("<div class='section' id='contact'><h3>Contact Me</h3><form>Send me a message:<br><input type='text' placeholder='Your Name'><br><input type='email' placeholder='Your Email'><br><textarea placeholder='Your Message'></textarea><br><button type='submit'>Send Message</button></form></div>", unsafe_allow_html=True)

# Add LinkedIn and Email links
st.markdown("""
### Or reach me on:
- [LinkedIn](https://www.linkedin.com/in/satyam-51a740102/)
- Email: satyam121satyam121@gmail.com
""")

# Footer
st.markdown("<div style='text-align:center; padding: 20px;'><p>&copy; 2024 Satyam - Senior Data Engineer</p></div>", unsafe_allow_html=True)
