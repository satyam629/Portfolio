import streamlit as st

# Set up the page layout and title
st.set_page_config(page_title="Satyam - Data Engineer Portfolio", layout="centered")

# Valid image URLs (SVG for AWS and PySpark, PNG for Snowflake)
aws_logo_url = "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg"
snowflake_logo_url = "https://logos-world.net/wp-content/uploads/2021/02/Snowflake-Logo-700x394.png"
pyspark_logo_url = "https://upload.wikimedia.org/wikipedia/commons/f/f3/Apache_Spark_logo.svg"

# Custom Styles for Animation
st.markdown(
    """
    <style>
    .fade-in {
        animation: fadeIn 1s ease-in forwards;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .hover-effect:hover {
        transform: scale(1.05);
        transition: transform 0.3s;
    }
    nav {
        background-color: #f0f0f0; 
        padding: 10px; 
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.title("Satyam", anchor="top")
st.subheader("Senior Data Engineer")
st.write("Bengaluru, India · +91 9031294999 · satyam121satyam121@gmail.com")

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
    st.image(aws_logo_url, caption="AWS", width=150, use_column_width=True, classes="hover-effect")
with col2:
    st.image(snowflake_logo_url, caption="Snowflake", width=150, use_column_width=True, classes="hover-effect")
with col3:
    st.image(pyspark_logo_url, caption="PySpark", width=150, use_column_width=True, classes="hover-effect")

# About Section
st.header("About Me", anchor="about")
st.markdown('<div class="fade-in">', unsafe_allow_html=True)
st.write("""
I am a Senior Data Engineer with 3+ years of experience, specializing in transitioning legacy data warehouses to Snowflake on AWS. 
I have expertise in AWS Glue, Snowpark, PySpark, and SQL, focusing on optimizing ETL pipelines for large-scale analytics.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
st.header("Skills", anchor="skills")
st.write("I have hands-on experience with the following technologies and tools:")

col1, col2, col3 = st.columns(3)
with col1:
    st.image(aws_logo_url, caption="AWS", width=100, use_column_width=True, classes="hover-effect")
with col2:
    st.image(snowflake_logo_url, caption="Snowflake", width=100, use_column_width=True, classes="hover-effect")
with col3:
    st.image(pyspark_logo_url, caption="PySpark", width=100, use_column_width=True, classes="hover-effect")

st.write("""
- **AWS Glue, S3, Redshift**: Building data pipelines, storing and transforming data.
- **Snowflake**: Data warehousing, Snowpark, advanced SQL for data processing.
- **PySpark**: Efficient processing of big data using partitioning, bucketing, and transformations.
- **SQL**: Strong command in SQL including pivoting, stored procedures, and optimizing data transformations.
""")

# Projects Section
st.header("Key Projects", anchor="projects")
st.subheader("Data Warehousing for BASF")
st.write("""
Optimized Snowflake data warehousing solutions, transforming large datasets using AWS Glue, achieving a 40% improvement in processing time.
""")
st.subheader("Cloud Migration for Pharmaceutical KPIs")
st.write("""
Led the migration of legacy data warehouses to Snowflake on AWS, ensuring minimal downtime and increased scalability.
""")

# Contact Section
st.header("Contact Me", anchor="contact")
with st.form("contact_form"):
    st.write("Send me a message:")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button(label="Send Message")

    if submit_button:
        st.success(f"Thank you {name}, your message has been sent!")

# Add LinkedIn and Email links
st.markdown("""
### Or reach me on:
- [LinkedIn](https://www.linkedin.com/in/satyam-51a740102/)
- Email: satyam121satyam121@gmail.com
""")

# Footer
st.markdown("""
<hr>
<p style="text-align:center;">&copy; 2024 Satyam - Senior Data Engineer</p>
""", unsafe_allow_html=True)
