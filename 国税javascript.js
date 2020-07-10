1-办税员登录
javascript: function click_tax(){$("#bsysf").click();var%20a%20=%20$("tr:contains('%E9%99%88%E5%88%A9%E9%94%8B')");a.click();var%20b%20=%20$("label");b[3].click();$("#yz-mm")[0].value%20=%20'a123456';$("#yz-login")[0].click();};click_tax();

2-1税单界面
javascript:function goto_tax(){window.location.href="https://etax.zhejiang.chinatax.gov.cn/zjgfdacx/sscx/wszmcy/wszm_cy.html"};goto_tax();

2-2下载税单
javascript:var a=['tr:contains(\x27','innerText','length','#40E0D0','value','#content>tr','click','backgroundColor','push','#queryBtn','from'];var%20b=function(c,d){c=c-0x0;var%20e=a[c];return%20e;};function%20downtax(){function%20c(){$('.bs-caret')[0x0][b('0x6')]();var%20e=$('span:contains(\x27%E5%B9%B4%E6%9C%88\x27)');e[0x0][b('0x6')]();var%20f=new%20Date();Y=f['getYear']()+0x76c;M=f['getMonth']()+0x1;Y_M=Y+'-'+'0'+M;sqrq_m[b('0x4')]=Y_M;};c();$(b('0x9'))[b('0x6')]();function%20d(){if($('div:contains(\x27%E8%A1%A8%E4%B8%AD%E6%95%B0%E6%8D%AE%E4%B8%BA%E7%A9%BA\x27)')[b('0x2')]!==0x4){var%20e=$(b('0x5'));arr=[];for(var%20f=0x0;f<e[b('0x2')];f++){arr[b('0x8')](e[f]['getElementsByTagName']('td')[0x0][b('0x1')]);}arr=Array[b('0xa')](new%20Set(arr));for(let%20k=0x0;k<arr[b('0x2')];k++){setTimeout(()=>{kjjks(arr[k]);},k*0x7d0);}for(var%20g=0x0;g<arr[b('0x2')];g++){var%20h=$(b('0x0')+arr[g]+'\x27)');h[0x0]['style'][b('0x7')]=b('0x3');}}};setTimeout(d,0xbb8);};downtax();

2-2(2)下载税单（手动选时间）
javascript:function markcolor(){ var tableBody = $('#content>tr');%20arr%20=%20[];%20for(var%20i=0;i<tableBody.length;i++){%20%20%20arr.push(tableBody[i].getElementsByTagName('td')[0].innerText)%20};%20arr=Array.from(new%20Set(arr));%20%20%20for(let%20j=0;j<arr.length;j++){%20%20%20setTimeout(()=>{%20%20%20%20%20%20kjjks(arr[j])%20%20%20},j*2000)%20};%20%20%20for(var%20j=0;j<arr.length;j++){%20%20%20var%20all_lines%20=%20$("tr:contains('"+arr[j]+"')");%20%20%20all_lines[0].style.backgroundColor='#40E0D0';%20};%20};%20markcolor();
