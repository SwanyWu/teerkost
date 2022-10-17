# Changelog

All notable changes to the project are documented here. There is no versioning for now. Just what is changed on what date.

# 17-10-2022

### Added
- CI pipeline: Code quality scanning with Pylint on every change.
- CI pipeline: Code coverage scanning on every change, including SVG badge in readme.

### Changed
- Refactor in parse_offers related to getting the right date (new module).
- Refactor in parse_offers related to price and deals (new module).

### Fixed
- Fixed many code quality issues that came up with Pylint.

# 07-10-2022

### Added
- Improved categorizing by text with multiple words and whitespace.
  
# 06-10-2022

### Changed
- Skip collecting the huge amount of non-food offers from 'Aldi'.

# 01-10-2022

### Fixed
- Fix for resetting scroll to top position when changing a filter.

# 30-09-2022

### Added
- Category filter for 'siroop'.

### Changed
- Combined two categories into 'zoetigheid'.
  
# 23-09-2022

### Fixed
- Fix for incomplete url when sharing a bookmarks list.
  
### Added
- Category filter for 'dier'.
- Category filter for 'sap'.
- Category filter for uncategorized offers.

# 10-09-2022

### Changed
- Deal text more consistent across shops.

# 04-09-2022

### Fixed
- Fix for wrong deal text from 'Spar'.
- Fix for no date or deal found from 'Lidl'.

# 23-07-2022

### Added
- Shop 'Spar' to the parser.
  
# 22-07-2022

### Added
- Shop 'Dirk' to the parser.

# 18-07-2022

### Added
- Clickable title to offers, to visit the shop homepage.
- Actual prices to offers from 'Lidl'.

### Changed
- Saving offers no longer disrupted when a shop is unreachable.

### Fixed
- Fix for not collecting data from 'Lidl'.
- For for unintentional clicks on donate button.

# 25-06-2022

### Added
- Ability to search for offers.

# 18-06-2022

### Fixed
- Fix for properly filling display width with items.

# 23-05-2022

### Fixed
- Fix for not collecting offers from 'Lidl' when only startdate is provided.
 
# 20-05-2022

### Changed
- Style of subtitle on page to be uniform across screen sizes.
  
# 18-05-2022

### Added
- Explainer text to no-bookmarks, nothing-found and 404 pages.
- Navigation bar and title to the 404 page.

### Fixed
- Fix when price sometimes is not shown for 'Plus'.

# 17-05-2022

### Added
- Junit style test reporting to be used by Github actions.

# 11-05-2022

### Changed
- App icons.

# 06-05-2022

### Changed
- Bottom navigation component on small screens.
- Home button on the bookmarks screen.

### Fixed
- Fix for wrong page title on other pages than home.
- Fix bottom padding for non‑rectangular displays.

# 02-05-2022

### Added
- Shop 'Plus' to the parser.

# 01-05-2022

### Changed
- Small color changes to the theme.
- Two column layout on small screens.

# 29-04-2022

### Added
- Displaying offers as list by id's, so the user can share bookmarks.

# 28-04-2022

### Changed
- Clean up more redundant text from product info.
- Small styling changes for the item cards.

### Fixed
- Fix for removing offer bookmarks that do not exist anymore.
  
# 26-04-2022

### Changed
- Item cards have a cleaner look.

### Fixed
- Fix for overflowing date label when item gets to small.

# 25-04-2022

### Added
- Copy the bookmarked offer as a shopping list.

# 24-04-2022

### Changed
- Wider sharing pop-up and added some information.

# 22-04-2022

### Changed
- Filters stay sticky when screenheight is big enough.

### Fixed
- Fix alignment of page on very large screens.
- Fix showing an empty filter without a category.

# 21-04-2022

### Added
- Category filter for 'gebak'.
- Category filter for 'tuin'.
- Visual feedback to copy-link when sharing the page.

### Fixed
- Fix for not finding offers from 'Aldi' when startday is not monday.

# 20-04-2022

### Added
- Clickable 'Teerkost' title added to the small screen version.

### Changed
- Sort offers according to the ordering of the filter labels.
- Refactor categories to seperate file.
- Clickable 'Teerkost' title always aligned to center of page.

# 19-04-2022

### Added
- Category filter for 'snoep'.

### Fixed
- Fix for not up-to-date state of bookmarked item when navigating.

### Changed
- Cleans up the offer info text a little better.

# 18-04-2022

### Added
- First version of bookmarking seperate offers, saving them locally in the browser.

### Fixed
- Fix for wrong validity period of 'AH' offers.
- Fix double "korting" label in some offers.

### Changed
- Size of date label on small screens.
- Show date instead of 'verlopen'.
- Removes redundant logo on share-dialog.
- Temporarily removes overlay with linking options on individual offers.
  
# 14-04-2022
### Fixed
- Fix for when 'Jumbo' does not provide an image.

### Added
- Unittests for collecting 'Ekoplaza' offers.

### Changed
- Provide a consistent product id to every offer item.
- Remove link to source code.
  
# 13-04-2022
### Added
- Category filter for 'ontbijt'.
- 'Load more' button for lazy loading and increased performance.
  
### Changed
- Sort filters buttons according to most used/important.

### Fixed
- Fix setting the wrong category when to-be-ignored word is found first.

# 12-04-2022
### Added
- Shop 'Ekoplaza' to the parser.
- Category filter for 'thee'.

# 11-04-2022
### Added
- Proper intention links for social media sharing.
- Date label to included 'verlopen' when offer is not current anymore.

# 10-04-2022
### Added
- Sharing dialog for browsers that do not support native sharing

# 08-04-2022
### Added
- Donation button
- Open Graph Protocol meta tags for rich social media sharing
- Update URL and page title according to the filters set

### Changed
- Move filters to the left when on a big enough screen

# 07-04-2022
### Added
- 404 'not-found' fallback page.

### Changed
- Design for displaying none-found and loading.

# 02-04-2022
### Added
- Numbering (amount of offers) to filter buttons.
- Words-to-be-ignored when categorizing products.
- Filter for 'frisdrank'.

# 31-03-2022
### Added
- Filter for 'wijn'.
- Filter for 'vlees'.





