<h1 align="center" style="transform: scale(1.2)">Foorma</h1>

<p align="center">
    <a href="#how-to-run-locally"> 
        <img src="https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-6A0DAD.svg?style=for-the-badge&logo=github&labelColor=555&logoColor=white" alt="In Progress">
    </a>
</p>

<p align="center">
    <a href="LICENSE">
        <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
    </a>
    <img src="https://img.shields.io/badge/Language%20%26%20Framework-Python%20%7C%20FastAPI-512DA8.svg?style=for-the-badge&logo=python" alt="Python / FastAPI">
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Stack-HTML%20%7C%20CSS%20%7C%20JS-F7DF1E.svg?style=for-the-badge&logo=javascript" alt="HTML / CSS / JS">
    <img src="https://img.shields.io/badge/Containerization-Docker-2496ED.svg?style=for-the-badge&logo=docker" alt="Docker">
    <img src="https://img.shields.io/badge/Server%20Host-AWS%20(Free%20Tier)-FF9900.svg?style=for-the-badge&logo=amazon-aws" alt="AWS">
</p>


<h2>
  <img src="" height="20">
  About the Project
</h2>

*This project is a study and practical application effort, developed with the objective of simulating a real product for personal use, in addition to validating and leveraging my professional skills in modern full-stack architecture.*
  *Understand better in the session: [Technologies Stack](#technologies-stack)*

**What I did:** 
  * ***Backend (API) Development***: I built a **high-performance** API in Python using **FastAPI**. The Backend is responsible for the core *conversion logic* and *crucial security measures*.
  * ***Complex Conversion Solution***: The most challenging conversion logic (DOCX to PDF) was solved by wrapping **LibreOffice Headless** inside the **Docker** container. This ensured the conversion environment was *stable* and reproducible on any server.
  * ***Security and Stability***: I implemented *file size validation* and used finally blocks to guarantee the immediate and automatic deletion of all user files after download, *prioritizing privacy*.
  * ***Practical, Zero-Cost Deployment***: For the deployment phase, the entire infrastructure was designed to be hosted on **AWS (Backend)** and **GitHub Pages (Frontend)**, and this integration is the next **big step**. Currently, the *focus* is on *stability* and final testing of the *conversion engine*.
  * ***Technological Focus***: The most valuable experience was in microservices orchestration, integrating **FastAPI (Backend)**, **Docker (Containerization)**, **LibreOffice (Conversion Engine)**, and **AWS/GitHub Pages (Infrastructure)** to deliver a ***complete and functional service***

---

<h2>
    <img src="" height="20"> Status & Tests (Developing)
</h2>

This project is actively under local development. The *full-stack* architecture (Frontend, API and Docker) has been completed, but the **final integration into the production environment (AWS and GitHub Pages)** has not yet started.

**!The service is not publicly accessible!**

To validate the project and test the conversion functionality (PDF ↔ DOCX), you must run it locally:
[**GO TO LOCAL TESTING INSTRUCTIONS**](#how-to-run-locally)

---

<h2>
    <img src="" height="20"> Roadmap & Future Implementations
</h2>

This project is actively maintained and has the following features planned for future releases:
1. ~~Architectural Development~~ [✓]
2. ~~Conversion Engine (Python/FastAPI)~~ [✓]
3. ~~Full User Interface (HTML/CSS/JS)~~ [✓]
4.  **Async Progress Bar** | Enhance the frontend to show a real-time progress bar instead of a simple status message during the conversion process.
5. **Infrastructure, Domain and HTTPS** | Deploy on AWS and GitHub Pages, acquire your own domain, and configure HTTPS.
6. **Format Expansion** | Add new conversions (ex: EPUB ↔ PDF).
7. **Monetization** | Implement Google AdSense in high traffic areas of the website.
8.  **Download Tracking** | Implement basic logging or analytics to monitor conversion usage and success rates.

---

<h2>
  <img src="" height="20">
  Technologies Stack
</h2>

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend API** | Python, **FastAPI** | High-performance API server and file handling. |
| **Conversion Core**| *pdf2docx*, **LibreOffice** | The engine for reliable document format changes. |
| **Infrastructure** | **Docker** | Guarantees consistent environment for complex tools. |
| **Frontend** | HTML, CSS, JavaScript | User interface and asynchronous API connection logic. |
| **Deployment** | AWS (Free Tier), **GitHub Pages** | Hosting the API and the static website for cost-efficiency. |

---

<h2>
  <img src="" height="20">
  How to Run Locally
</h2>

If you wish to run the frontend locally and connect it to your running Docker API:

1.  Clone this repository.
2.  Ensure your **Converter API** Docker container is running on ***http://localhost:8000***.
3.  Navigate to the **frontend** directory in your terminal.
    ```bash
    cd project && cd frontend
    ```
4.  Start a local HTTP server:
    ```bash
    python -m http.server 8080
    #or
    python3 -m http.server 8080
    ```
5.  Access the app at ***http://localhost:8080***.

<h2>
  <img src="" height="20">
  Contribution
</h2>

*Contributions are welcome! If you have ideas or suggestions, feel free to open an issue or send a pull request.*

<h2>
  <img src="" height="20">
  License
</h2>

This project is under the MIT license. For more details, see the [LICENSE](LICENSE) file.
