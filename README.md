## Task Description
Develop a public API that returns the following infromation in JSON format

1. **your registered email address** (used to register on the HNG12 Slack workspace).
2. The current datetime as an ISO 8601 formatted timestamp
3. The GitHub URl of the project's codebase

## Requirements
1. Technology Stack:
	- **Programming Language/Framework**: Use any of the following; See Sharp (C#), PHP, Python, Go, Java, Javascript/TypeScript.
	- **Deployment**: The API must be deployed to a publicly accessible endpoint.
	- **CORS Handling**: Ensure the API handles Cross-Origin Resource Sharing (CORS) appropriately.
	- **Response Format**: All responses must be in JSON format.

2. Version Control:
	- **Repository Hosting**: Host the code on GitHub.
	- **Repository Visibility**: The repository must be public.
	- **Documentation**: Include a well-structured README.md file

## API Specification
- Endpoint: GET\*\* <your-url>
- Required JSON Response Format (200 OK):

## Acceptance Criteria
###Functionality

- The API must accept GET requests and return the required JSON response
- The current_datetime field must be dynamically generated in ISo 8601 format (UTC)
- Provides appropriate HTTP status code

### Code Quality
- Organized code structure

### Documentation
- README.md must include:
	- A clear description of the project.
	- Setup instructions (e.g., how to run teh project locally)
- API documentation including:
	- Endpoint URL
	- Request/response format.
	- Example usage
- One backlink related to your chosen programming language/stack:
