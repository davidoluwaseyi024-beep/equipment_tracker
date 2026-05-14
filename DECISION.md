# Decisions

## Purpose
This project tracks equipment maintenance dates and highlights overdue items.

## Main decisions
- Used Django because it is fast for building database-backed apps.
- Used one `Equipment` model to keep the project simple.
- Used Django admin for data entry instead of a custom form system.
- Added an overdue badge to make status visible at a glance.
- Kept styling simple with plain HTML and CSS for easier maintenance.

## Trade-offs
- The app is simple and not meant for production use.
- The design focuses on clarity rather than advanced features.

## Future improvements
- Add authentication for users.
- Add search and filters on the front-end.
- Add CSV export.
- Improve mobile responsiveness.