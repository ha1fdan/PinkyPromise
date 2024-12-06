# Pinky Promise 🤙

Pinky Promise is a simple Flask application for creating, viewing, and signing promises. Each promise has a description, a due date, and a list of signatures.

## Features

- **Create Promises:** Add a new promise with a description, due date, and creator's name.
- **Sign Promises:** Sign promises before the due date.
- **View Promises:** See the details of a promise and its signatures.
- **404 Page:** Custom error page for non-existent routes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pinky-promise.git
   cd pinky-promise
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Project Structure

```
pinky-promise/
│
├── app.py
├── templates/
│   ├── 404.html
│   ├── base.html
│   ├── create_promise.html
│   └── view_promise.html
├── promises.json
├── requirements.txt
└── README.md
```

## Dependencies

- Flask
- Tailwind CSS (via CDN)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to your forked repository: `git push origin feature-name`.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Built with 💖 and Flask.