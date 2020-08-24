# beastify

## What it does ##

运行顺序：
1. 注入content script(一般是监听到事件后才注入，这里可能并不符合真实体验)
  > browser.tabs.executeScript({file: "/content_scripts/beastify.js"})

2. 开始监听事件
	- `if (e.target.classList.contains("beast"))` 则激活当前页，并调用`beastify()`
	- `else if (e.target.classList.contains("reset"))`,财调用`reset()`,恢复网页

3. 调用`beastify()`
	- `browser.tabs.insertCSS({code: hidePage})`,把所有`class`不为`beastify-image`的元素都隐藏
	- `browser.extension.getURL`得到点击目标对应的图片URL
	- ```browser.tabs.sendMessage(tabs[0].id, {
          command: "beastify",
          beastURL: url
        })```
        向content script发生message。
4. 或调用`reset()`
	- 原理一样

5. content script接收message
	- `browser.runtime.onMessage.addListener((message) => {}`
	
6. 调用`insertBeast(beastURL)`或`removeExistingBeasts()`


The extension includes:

* a browser action with a popup including HTML, CSS, and JS
* a content script
* three images, each of a different beast, packaged as web accessible resources

When the user clicks the browser action button, the popup is shown, enabling
the user to choose one of three beasts.

When it is shown, the popup injects a content script into the current page.

When the user chooses a beast, the extension sends the content script a message containing
the name of the chosen beast.

When the content script receives this message, it replaces the current page
content with an image of the chosen beast.

When the user clicks the reset button, the page reloads, and reverts to its original form.

Note that:

* if the user reloads the tab, or switches tabs, while the popup is open, then the popup won't be able to beastify the page any more (because the content script was injected into the original tab).

* by default [`tabs.executeScript()`](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/API/tabs/executeScript) injects the script only when the web page and its resources have finished loading. This means that clicks in the popup will have no effect until the page has finished loading.

* it's not possible to inject content scripts into certain pages, including privileged browser pages like "about:debugging" and the [addons.mozilla.org](https://addons.mozilla.org/) website. If the user clicks the beastify icon when such a page is loaded into the active tab, the popup displays an error message.

## What it shows ##

* write a browser action with a popup
* how to have different browser_action images based upon the theme
* give the popup style and behavior using CSS and JS
* inject a content script programmatically using `tabs.executeScript()`
* send a message from the main extension to a content script
* use web accessible resources to enable web pages to load packaged content
* reload web pages
