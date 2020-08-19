

// 税单查询界面，输入验证码后，自动填当月日期并下载。


	function select_date(){
		$(".bs-caret")[0].click();
		var a = $("span:contains('年月')");
		a[0].click();

		var Da = new Date();
		Y = Da.getYear() + 1900;
		M = Da.getMonth() + 1;
		Y_M = Y +"-" + "0" + M;

		$("#sqrq_m")[0].value = Y_M;
	};
	select_date();

	$("#queryBtn").click();

	
	function markcolor(){
		if ($("div:contains('表中数据为空')").length !== 4) {
			var tableBody = $('#content>tr');
			arr = [];
			for(var i=0;i<tableBody.length;i++){
			  arr.push(tableBody[i].getElementsByTagName('td')[0].innerText)
			}
			arr=Array.from(new Set(arr))


			// for(let j=0;j<arr.length;j++){
			//   setTimeout(()=>{
			//      kjjks(arr[j])
			//   },j*2000)
			// }
			// 不能使用页面自带的kjjks()函数

			// for(let j=0;j<arr.length;j++){
  	// 		var c = $("#content a")
			//   setTimeout(()=>{
			//      c[j].click()
			//   },j*2000)
			// }
			for(let j=0;j<arr.length;j++){
			  // var all_lines = $("tr:contains('"+arr[j]+"')");
			  setTimeout(()=>{
			  	var all_lines = $("tr:contains('"+arr[j]+"')");
			    all_lines[0].getElementsByTagName("a")[0].click();
			  },j*2000);
			  
			}



			for(var j=0;j<arr.length;j++){
			  var all_lines = $("tr:contains('"+arr[j]+"')");
			  all_lines[0].style.backgroundColor='#40E0D0';
			}
		}
	};

	
	setTimeout(markcolor,3000) //settimeout前面套if，运行不起来，markcolor没有()
		
	

	// $("#content>tr")[0].innerText