browser.contextMenus.create({
  id: "taxLogin",
  title: "1-办税员登录"
});

browser.contextMenus.onClicked.addListener(function(info, tab) {
  if (info.menuItemId == "taxLogin") {
  	// browser.tabs.executeScript({file:"jquery-3.5.1.min.js"});
  	// 上句引入jquery,直接写在这里，下句没效果
  	// 把juqery通过manifest.json的content_script引入，所有脚本都可
  	// 直接引用jquery.
    browser.tabs.executeScript({file:"taxLogin.js"});
  }
});



// 右键权限：
// "permissions": [
//     "contextMenus"
//   ]

// background.js是如何创建右键菜单，并调用content script

// content script中涉及到引用“Jquery”的，需先引入Jquery包
// browser.tabs.executeScript({file:"jquery-3.5.1.min.js"});