## Task Overview

A fast-growing SaaS product enables users to manage their personal profiles. When a user updates their profile, the business requires that they receive a confirmation email. However, updating the profile currently does not result in email notifications being delivered, and the support team reports frustrated users. Your job is to implement and validate the necessary asynchronous background task integration so every user receives a confirmation email reliably after updating their information, without slowing down the API responsiveness.

## Guidance

- Follow FastAPI asynchronous best practices and ensure non-blocking request handling.
- Structure the background task so emails send after profile persistence, with clear separation from main request workflow.
- Use dependency injection for background tasks and simulate email logic if needed through basic logging or print statements instead of actual email delivery.
- Ensure that the user experience remains fast—no slowdowns or waiting for email delivery.
- Handle any potential issues in async task invocation to guarantee repeatable, observable notifications for every profile update.
- Use robust error handling to avoid silent failures in email notification delivery logic.
- Environment configuration, such as email credentials, should not be hardcoded.

## Objectives

- Properly integrate FastAPI's BackgroundTasks so that email notifications are reliably triggered post-profile-update.
- Guarantee all async endpoints and background flows do not block or delay the main request/response cycle.
- Simulate email notification logic such that it's easily verifiable on each update.
- Use Pydantic models for payload validation and response, avoiding any exposure of sensitive data.
- Ensure all error handling and async flows adhere to best practices and are observable through logs or console output.

## How to Verify

- Update a user profile and observe confirmation of the email notification logic executing after the HTTP response.
- Verify API responsiveness—the response for the profile update returns immediately, and email logic executes separately.
- Check logs or output to ensure every successful profile update reliably triggers an email action.
- Confirm that error scenarios, such as failures in the email logic, are handled gracefully without impacting user profile updates.
- Review that no sensitive user data is exposed in responses or logs.