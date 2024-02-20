
# Quiz Trainer Browser for Exams 🚀

Welcome to the Quiz Trainer Browser, your dynamic tool for mastering exam questions across a variety of subjects. Designed to enhance your study sessions, our platform offers an interactive way to navigate, search, and engage with exam questions. Whether you're aiming to conquer specific certifications or just broadening your knowledge, this tool adapts to your learning journey.

## Features 🌟

- **Navigation Controls:** Seamlessly move between questions using the `Previous` and `Next` buttons.
- **Search Capability:** Directly jump to a question by entering its number in the search bar, making your review sessions more efficient.
- **Dynamic Question Loading:** Questions are loaded dynamically from a JSON file, ensuring that the content stays up-to-date and relevant.

## Getting Started 🛠️

To get started with the Quiz Trainer Browser, you will need to set up your environment.

### Prerequisites

Ensure you have Python installed on your system. This project is built using PyQt5, so Python is a must-have.

### Installation

1. Clone this repository or download the source code to your local machine.
2. Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

3. Once the dependencies are installed, you can start the application by running:

```bash
python main.py <json_file_path>
```

For example, to start the application with the AWS DevOps Professional exam questions, you can run:

```bash
python main.py ./resources/questions/aws_devops_professional.json
```

This command initializes the application, presenting you with an interactive browser interface showcasing the exam questions.

## Usage 📚

The application interface is straightforward:

- Use the `Previous` and `Next` buttons on the toolbar to navigate through the questions.
- To jump to a specific question, enter the question number in the search bar and press Enter.
- If the entered question number does not exist, a warning message will appear, prompting you to try again.

## Current Exams Available 📋

- AWS Certified DevOps Engineer - Professional

Stay tuned as we continue to add more exams to our collection!

## Do You Want to See More Exams? 💡

We thrive on community contributions! If you're eager to expand our quiz universe with more topics, kindly let us know by opening an issue on this repository. Your input helps us grow and improve!

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Thanks to everyone who has contributed to the development and improvement of this project.

Let's ace that exam together! 🎓
