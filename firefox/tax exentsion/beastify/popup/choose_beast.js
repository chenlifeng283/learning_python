/**
 * CSS to hide everything on the page,
 * except for elements that have the "beastify-image" class.
 */
 // 选取除了 class=".beastify-image" 元素以外的所有元素,并隐藏
const hidePage = `body > :not(.beastify-image) {
                    display: none;
                  }`;

/**
 * Listen for clicks on the buttons, and send the appropriate message to
 * the content script in the page.
 */
/*监听buttons的click动作，传递message到content script,
 content script是当前网页的脚本，这里代码的作用类似于直接在
 控制台输入代码，影响当前网页
 */
function listenForClicks() {
  document.addEventListener("click", (e) => {

    /**
     * Given the name of a beast, get the URL to the corresponding image.
     根据beastName参数定位相应的URL地址
     */
    function beastNameToURL(beastName) {
      switch (beastName) {
        case "Frog":
          return browser.extension.getURL("beasts/frog.jpg");
        case "Snake":
          return browser.extension.getURL("beasts/snake.jpg");
        case "Turtle":
          return browser.extension.getURL("beasts/turtle.jpg");
      }
    }

    /**
     * Insert the page-hiding CSS into the active tab,
     * then get the beast URL and
     * send a "beastify" message to the content script in the active tab.
     用insertCss API修改css,隐藏当前页
     调用beastNameToURL()获取‘点击目标’的URL
     发送“beastify"信息给content script.
     */
    function beastify(tabs) {
      browser.tabs.insertCSS({code: hidePage}).then(() => {
        let url = beastNameToURL(e.target.textContent);
        browser.tabs.sendMessage(tabs[0].id, {
          command: "beastify",
          beastURL: url
        });
      });
    }

    /**
     * Remove the page-hiding CSS from the active tab,
     * send a "reset" message to the content script in the active tab.
     按下reset按钮后恢复当前页面，原理同beastify(),
     */
    function reset(tabs) {
      browser.tabs.removeCSS({code: hidePage}).then(() => {
        browser.tabs.sendMessage(tabs[0].id, {
          command: "reset",
        });
      });
    }

    /**
     * Just log the error to the console.
     */
    function reportError(error) {
      console.error(`Could not beastify: ${error}`);
    }

    /**
     * Get the active tab,
     * then call "beastify()" or "reset()" as appropriate.
     ”点击“后开始运行程序的第二源头
     如果点击了class='beast'的三个按钮就运行beastify()
     如果点击了class='reset'的按钮就运行reset.
     */
    if (e.target.classList.contains("beast")) {
      browser.tabs.query({active: true, currentWindow: true})
        .then(beastify)
        .catch(reportError);
    }
    else if (e.target.classList.contains("reset")) {
      browser.tabs.query({active: true, currentWindow: true})
        .then(reset)
        .catch(reportError);
    }
  });
}

/**
 * There was an error executing the script.
 * Display the popup's error message, and hide the normal UI.
 */
function reportExecuteScriptError(error) {
  document.querySelector("#popup-content").classList.add("hidden");
  document.querySelector("#error-content").classList.remove("hidden");
  console.error(`Failed to execute beastify content script: ${error.message}`);
}

/**
 * When the popup loads, inject a content script into the active tab,
 * and add a click handler.
 * If we couldn't inject the script, handle the error.
注入content script ,然后开始listenForClicks监听click事件
 */
browser.tabs.executeScript({file: "/content_scripts/beastify.js"})
.then(listenForClicks)
.catch(reportExecuteScriptError);
