<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "58PYcNO9J8jdcRuj5DsCyfy4jKw:1366668602971";
 
 
 var CS_env = {"projectHomeUrl":"/p/chordimplementation","loggedInUserEmail":"ethan.wjj@gmail.com","token":"58PYcNO9J8jdcRuj5DsCyfy4jKw:1366668602971","domainName":null,"profileUrl":"/u/115244174812975043353/","projectName":"chordimplementation","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/13714586478408612229","relativeBaseUrl":"","assetHostPath":"https://ssl.gstatic.com/codesite/ph"};
 var _gaq = _gaq || [];
 _gaq.push(
 ['siteTracker._setAccount', 'UA-18071-1'],
 ['siteTracker._trackPageview']);
 
 (function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(ga);
 })();
 
 </script>
 
 
 <title>__init__.py - 
 chordimplementation -
 
 
 implementation in python of chord DHT - Google Project Hosting
 </title>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13714586478408612229/css/core.css">
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13714586478408612229/css/ph_detail.css" >
 
 
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13714586478408612229/css/d_sb.css" >
 
 
 
<!--[if IE]>
 <link type="text/css" rel="stylesheet" href="https://ssl.gstatic.com/codesite/ph/13714586478408612229/css/d_ie.css" >
<![endif]-->
 <style type="text/css">
 .menuIcon.off { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -42px }
 .menuIcon.on { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 -28px }
 .menuIcon.down { background: no-repeat url(https://ssl.gstatic.com/codesite/ph/images/dropdown_sprite.gif) 0 0; }
 
 
 
  tr.inline_comment {
 background: #fff;
 vertical-align: top;
 }
 div.draft, div.published {
 padding: .3em;
 border: 1px solid #999; 
 margin-bottom: .1em;
 font-family: arial, sans-serif;
 max-width: 60em;
 }
 div.draft {
 background: #ffa;
 } 
 div.published {
 background: #e5ecf9;
 }
 div.published .body, div.draft .body {
 padding: .5em .1em .1em .1em;
 max-width: 60em;
 white-space: pre-wrap;
 white-space: -moz-pre-wrap;
 white-space: -pre-wrap;
 white-space: -o-pre-wrap;
 word-wrap: break-word;
 font-size: 1em;
 }
 div.draft .actions {
 margin-left: 1em;
 font-size: 90%;
 }
 div.draft form {
 padding: .5em .5em .5em 0;
 }
 div.draft textarea, div.published textarea {
 width: 95%;
 height: 10em;
 font-family: arial, sans-serif;
 margin-bottom: .5em;
 }

 
 .nocursor, .nocursor td, .cursor_hidden, .cursor_hidden td {
 background-color: white;
 height: 2px;
 }
 .cursor, .cursor td {
 background-color: darkblue;
 height: 2px;
 display: '';
 }
 
 
.list {
 border: 1px solid white;
 border-bottom: 0;
}

 
 </style>
</head>
<body class="t4">
<script type="text/javascript">
 window.___gcfg = {lang: 'en'};
 (function() 
 {var po = document.createElement("script");
 po.type = "text/javascript"; po.async = true;po.src = "https://apis.google.com/js/plusone.js";
 var s = document.getElementsByTagName("script")[0];
 s.parentNode.insertBefore(po, s);
 })();
</script>
<div class="headbg">

 <div id="gaia">
 

 <span>
 
 
 
 <a href="#" id="multilogin-dropdown" onclick="return false;"
 ><u><b>ethan.wjj@gmail.com</b></u> <small>&#9660;</small></a>
 
 
 | <a href="/u/115244174812975043353/" id="projects-dropdown" onclick="return false;"
 ><u>My favorites</u> <small>&#9660;</small></a>
 | <a href="/u/115244174812975043353/" onclick="_CS_click('/gb/ph/profile');"
 title="Profile, Updates, and Settings"
 ><u>Profile</u></a>
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fchordimplementation%2Fsource%2Fbrowse%2Ftrunk%2FChordImplementation%2Fsrc%2FChordControl%2F__init__.py" 
 onclick="_CS_click('/gb/ph/signout');"
 ><u>Sign out</u></a>
 
 </span>

 </div>

 <div class="gbh" style="left: 0pt;"></div>
 <div class="gbh" style="right: 0pt;"></div>
 
 
 <div style="height: 1px"></div>
<!--[if lte IE 7]>
<div style="text-align:center;">
Your version of Internet Explorer is not supported. Try a browser that
contributes to open source, such as <a href="http://www.firefox.com">Firefox</a>,
<a href="http://www.google.com/chrome">Google Chrome</a>, or
<a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.
</div>
<![endif]-->



 <table style="padding:0px; margin: 0px 0px 10px 0px; width:100%" cellpadding="0" cellspacing="0"
 itemscope itemtype="http://schema.org/CreativeWork">
 <tr style="height: 58px;">
 
 
 
 <td id="plogo">
 <link itemprop="url" href="/p/chordimplementation">
 <a href="/p/chordimplementation/">
 
 <img src="https://ssl.gstatic.com/codesite/ph/images/defaultlogo.png" alt="Logo" itemprop="image">
 
 </a>
 </td>
 
 <td style="padding-left: 0.5em">
 
 <div id="pname">
 <a href="/p/chordimplementation/"><span itemprop="name">chordimplementation</span></a>
 </div>
 
 <div id="psum">
 <a id="project_summary_link"
 href="/p/chordimplementation/"><span itemprop="description">implementation in python of chord DHT</span></a>
 
 </div>
 
 
 </td>
 <td style="white-space:nowrap;text-align:right; vertical-align:bottom;">
 
 <form action="/hosting/search">
 <input size="30" name="q" value="" type="text">
 
 <input type="submit" name="projectsearch" value="Search projects" >
 </form>
 
 </tr>
 </table>

</div>

 
<div id="mt" class="gtb"> 
 <a href="/p/chordimplementation/" class="tab ">Project&nbsp;Home</a>
 
 
 
 
 <a href="/p/chordimplementation/downloads/list" class="tab ">Downloads</a>
 
 
 
 
 
 <a href="/p/chordimplementation/w/list" class="tab ">Wiki</a>
 
 
 
 
 
 <a href="/p/chordimplementation/issues/list"
 class="tab ">Issues</a>
 
 
 
 
 
 <a href="/p/chordimplementation/source/checkout"
 class="tab active">Source</a>
 
 
 
 
 
 
 
 
 <div class=gtbc></div>
</div>
<table cellspacing="0" cellpadding="0" width="100%" align="center" border="0" class="st">
 <tr>
 
 
 
 
 
 
 <td class="subt">
 <div class="st2">
 <div class="isf">
 
 


 <span class="inst1"><a href="/p/chordimplementation/source/checkout">Checkout</a></span> &nbsp;
 <span class="inst2"><a href="/p/chordimplementation/source/browse/">Browse</a></span> &nbsp;
 <span class="inst3"><a href="/p/chordimplementation/source/list">Changes</a></span> &nbsp;
 
 
 
 
 
 
 
 </form>
 <script type="text/javascript">
 
 function codesearchQuery(form) {
 var query = document.getElementById('q').value;
 if (query) { form.action += '%20' + query; }
 }
 </script>
 </div>
</div>

 </td>
 
 
 
 <td align="right" valign="top" class="bevel-right"></td>
 </tr>
</table>


<script type="text/javascript">
 var cancelBubble = false;
 function _go(url) { document.location = url; }
</script>
<div id="maincol"
 
>

 




<div class="expand">
<div id="colcontrol">
<style type="text/css">
 #file_flipper { white-space: nowrap; padding-right: 2em; }
 #file_flipper.hidden { display: none; }
 #file_flipper .pagelink { color: #0000CC; text-decoration: underline; }
 #file_flipper #visiblefiles { padding-left: 0.5em; padding-right: 0.5em; }
</style>
<table id="nav_and_rev" class="list"
 cellpadding="0" cellspacing="0" width="100%">
 <tr>
 
 <td nowrap="nowrap" class="src_crumbs src_nav" width="33%">
 <strong class="src_nav">Source path:&nbsp;</strong>
 <span id="crumb_root">
 
 <a href="/p/chordimplementation/source/browse/">svn</a>/&nbsp;</span>
 <span id="crumb_links" class="ifClosed"><a href="/p/chordimplementation/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/">ChordImplementation</a><span class="sp">/&nbsp;</span><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/">src</a><span class="sp">/&nbsp;</span><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/">ChordControl</a><span class="sp">/&nbsp;</span>__init__.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/__init__.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/__init__.py?r=40" title="Previous">&lsaquo;r40</a></li>
 
 </ul>
 </td>
 
 <td class="flipper"><b>r41</b></td>
 
 </tr></table>
 </td> 
 </tr>
</table>

<div class="fc">
 
 
 
<style type="text/css">
.undermouse span {
 background-image: url(https://ssl.gstatic.com/codesite/ph/images/comments.gif); }
</style>
<table class="opened" id="review_comment_area"
><tr>
<td id="nums">
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
<pre><table width="100%" id="nums_table_0"><tr id="gr_svn41_1"

><td id="1"><a href="#1">1</a></td></tr
><tr id="gr_svn41_2"

><td id="2"><a href="#2">2</a></td></tr
><tr id="gr_svn41_3"

><td id="3"><a href="#3">3</a></td></tr
><tr id="gr_svn41_4"

><td id="4"><a href="#4">4</a></td></tr
><tr id="gr_svn41_5"

><td id="5"><a href="#5">5</a></td></tr
><tr id="gr_svn41_6"

><td id="6"><a href="#6">6</a></td></tr
><tr id="gr_svn41_7"

><td id="7"><a href="#7">7</a></td></tr
><tr id="gr_svn41_8"

><td id="8"><a href="#8">8</a></td></tr
><tr id="gr_svn41_9"

><td id="9"><a href="#9">9</a></td></tr
><tr id="gr_svn41_10"

><td id="10"><a href="#10">10</a></td></tr
><tr id="gr_svn41_11"

><td id="11"><a href="#11">11</a></td></tr
><tr id="gr_svn41_12"

><td id="12"><a href="#12">12</a></td></tr
><tr id="gr_svn41_13"

><td id="13"><a href="#13">13</a></td></tr
><tr id="gr_svn41_14"

><td id="14"><a href="#14">14</a></td></tr
><tr id="gr_svn41_15"

><td id="15"><a href="#15">15</a></td></tr
><tr id="gr_svn41_16"

><td id="16"><a href="#16">16</a></td></tr
><tr id="gr_svn41_17"

><td id="17"><a href="#17">17</a></td></tr
><tr id="gr_svn41_18"

><td id="18"><a href="#18">18</a></td></tr
><tr id="gr_svn41_19"

><td id="19"><a href="#19">19</a></td></tr
><tr id="gr_svn41_20"

><td id="20"><a href="#20">20</a></td></tr
><tr id="gr_svn41_21"

><td id="21"><a href="#21">21</a></td></tr
><tr id="gr_svn41_22"

><td id="22"><a href="#22">22</a></td></tr
><tr id="gr_svn41_23"

><td id="23"><a href="#23">23</a></td></tr
><tr id="gr_svn41_24"

><td id="24"><a href="#24">24</a></td></tr
><tr id="gr_svn41_25"

><td id="25"><a href="#25">25</a></td></tr
><tr id="gr_svn41_26"

><td id="26"><a href="#26">26</a></td></tr
><tr id="gr_svn41_27"

><td id="27"><a href="#27">27</a></td></tr
><tr id="gr_svn41_28"

><td id="28"><a href="#28">28</a></td></tr
><tr id="gr_svn41_29"

><td id="29"><a href="#29">29</a></td></tr
><tr id="gr_svn41_30"

><td id="30"><a href="#30">30</a></td></tr
><tr id="gr_svn41_31"

><td id="31"><a href="#31">31</a></td></tr
><tr id="gr_svn41_32"

><td id="32"><a href="#32">32</a></td></tr
><tr id="gr_svn41_33"

><td id="33"><a href="#33">33</a></td></tr
><tr id="gr_svn41_34"

><td id="34"><a href="#34">34</a></td></tr
><tr id="gr_svn41_35"

><td id="35"><a href="#35">35</a></td></tr
><tr id="gr_svn41_36"

><td id="36"><a href="#36">36</a></td></tr
><tr id="gr_svn41_37"

><td id="37"><a href="#37">37</a></td></tr
><tr id="gr_svn41_38"

><td id="38"><a href="#38">38</a></td></tr
><tr id="gr_svn41_39"

><td id="39"><a href="#39">39</a></td></tr
><tr id="gr_svn41_40"

><td id="40"><a href="#40">40</a></td></tr
><tr id="gr_svn41_41"

><td id="41"><a href="#41">41</a></td></tr
><tr id="gr_svn41_42"

><td id="42"><a href="#42">42</a></td></tr
><tr id="gr_svn41_43"

><td id="43"><a href="#43">43</a></td></tr
><tr id="gr_svn41_44"

><td id="44"><a href="#44">44</a></td></tr
><tr id="gr_svn41_45"

><td id="45"><a href="#45">45</a></td></tr
><tr id="gr_svn41_46"

><td id="46"><a href="#46">46</a></td></tr
><tr id="gr_svn41_47"

><td id="47"><a href="#47">47</a></td></tr
><tr id="gr_svn41_48"

><td id="48"><a href="#48">48</a></td></tr
><tr id="gr_svn41_49"

><td id="49"><a href="#49">49</a></td></tr
><tr id="gr_svn41_50"

><td id="50"><a href="#50">50</a></td></tr
><tr id="gr_svn41_51"

><td id="51"><a href="#51">51</a></td></tr
><tr id="gr_svn41_52"

><td id="52"><a href="#52">52</a></td></tr
><tr id="gr_svn41_53"

><td id="53"><a href="#53">53</a></td></tr
><tr id="gr_svn41_54"

><td id="54"><a href="#54">54</a></td></tr
><tr id="gr_svn41_55"

><td id="55"><a href="#55">55</a></td></tr
><tr id="gr_svn41_56"

><td id="56"><a href="#56">56</a></td></tr
><tr id="gr_svn41_57"

><td id="57"><a href="#57">57</a></td></tr
><tr id="gr_svn41_58"

><td id="58"><a href="#58">58</a></td></tr
><tr id="gr_svn41_59"

><td id="59"><a href="#59">59</a></td></tr
><tr id="gr_svn41_60"

><td id="60"><a href="#60">60</a></td></tr
><tr id="gr_svn41_61"

><td id="61"><a href="#61">61</a></td></tr
><tr id="gr_svn41_62"

><td id="62"><a href="#62">62</a></td></tr
><tr id="gr_svn41_63"

><td id="63"><a href="#63">63</a></td></tr
><tr id="gr_svn41_64"

><td id="64"><a href="#64">64</a></td></tr
><tr id="gr_svn41_65"

><td id="65"><a href="#65">65</a></td></tr
><tr id="gr_svn41_66"

><td id="66"><a href="#66">66</a></td></tr
><tr id="gr_svn41_67"

><td id="67"><a href="#67">67</a></td></tr
><tr id="gr_svn41_68"

><td id="68"><a href="#68">68</a></td></tr
><tr id="gr_svn41_69"

><td id="69"><a href="#69">69</a></td></tr
><tr id="gr_svn41_70"

><td id="70"><a href="#70">70</a></td></tr
><tr id="gr_svn41_71"

><td id="71"><a href="#71">71</a></td></tr
><tr id="gr_svn41_72"

><td id="72"><a href="#72">72</a></td></tr
><tr id="gr_svn41_73"

><td id="73"><a href="#73">73</a></td></tr
><tr id="gr_svn41_74"

><td id="74"><a href="#74">74</a></td></tr
><tr id="gr_svn41_75"

><td id="75"><a href="#75">75</a></td></tr
><tr id="gr_svn41_76"

><td id="76"><a href="#76">76</a></td></tr
><tr id="gr_svn41_77"

><td id="77"><a href="#77">77</a></td></tr
><tr id="gr_svn41_78"

><td id="78"><a href="#78">78</a></td></tr
><tr id="gr_svn41_79"

><td id="79"><a href="#79">79</a></td></tr
><tr id="gr_svn41_80"

><td id="80"><a href="#80">80</a></td></tr
><tr id="gr_svn41_81"

><td id="81"><a href="#81">81</a></td></tr
><tr id="gr_svn41_82"

><td id="82"><a href="#82">82</a></td></tr
><tr id="gr_svn41_83"

><td id="83"><a href="#83">83</a></td></tr
><tr id="gr_svn41_84"

><td id="84"><a href="#84">84</a></td></tr
><tr id="gr_svn41_85"

><td id="85"><a href="#85">85</a></td></tr
><tr id="gr_svn41_86"

><td id="86"><a href="#86">86</a></td></tr
><tr id="gr_svn41_87"

><td id="87"><a href="#87">87</a></td></tr
><tr id="gr_svn41_88"

><td id="88"><a href="#88">88</a></td></tr
><tr id="gr_svn41_89"

><td id="89"><a href="#89">89</a></td></tr
><tr id="gr_svn41_90"

><td id="90"><a href="#90">90</a></td></tr
><tr id="gr_svn41_91"

><td id="91"><a href="#91">91</a></td></tr
><tr id="gr_svn41_92"

><td id="92"><a href="#92">92</a></td></tr
><tr id="gr_svn41_93"

><td id="93"><a href="#93">93</a></td></tr
><tr id="gr_svn41_94"

><td id="94"><a href="#94">94</a></td></tr
><tr id="gr_svn41_95"

><td id="95"><a href="#95">95</a></td></tr
><tr id="gr_svn41_96"

><td id="96"><a href="#96">96</a></td></tr
><tr id="gr_svn41_97"

><td id="97"><a href="#97">97</a></td></tr
><tr id="gr_svn41_98"

><td id="98"><a href="#98">98</a></td></tr
><tr id="gr_svn41_99"

><td id="99"><a href="#99">99</a></td></tr
><tr id="gr_svn41_100"

><td id="100"><a href="#100">100</a></td></tr
><tr id="gr_svn41_101"

><td id="101"><a href="#101">101</a></td></tr
><tr id="gr_svn41_102"

><td id="102"><a href="#102">102</a></td></tr
><tr id="gr_svn41_103"

><td id="103"><a href="#103">103</a></td></tr
><tr id="gr_svn41_104"

><td id="104"><a href="#104">104</a></td></tr
><tr id="gr_svn41_105"

><td id="105"><a href="#105">105</a></td></tr
><tr id="gr_svn41_106"

><td id="106"><a href="#106">106</a></td></tr
><tr id="gr_svn41_107"

><td id="107"><a href="#107">107</a></td></tr
><tr id="gr_svn41_108"

><td id="108"><a href="#108">108</a></td></tr
><tr id="gr_svn41_109"

><td id="109"><a href="#109">109</a></td></tr
><tr id="gr_svn41_110"

><td id="110"><a href="#110">110</a></td></tr
><tr id="gr_svn41_111"

><td id="111"><a href="#111">111</a></td></tr
><tr id="gr_svn41_112"

><td id="112"><a href="#112">112</a></td></tr
><tr id="gr_svn41_113"

><td id="113"><a href="#113">113</a></td></tr
><tr id="gr_svn41_114"

><td id="114"><a href="#114">114</a></td></tr
><tr id="gr_svn41_115"

><td id="115"><a href="#115">115</a></td></tr
><tr id="gr_svn41_116"

><td id="116"><a href="#116">116</a></td></tr
><tr id="gr_svn41_117"

><td id="117"><a href="#117">117</a></td></tr
><tr id="gr_svn41_118"

><td id="118"><a href="#118">118</a></td></tr
><tr id="gr_svn41_119"

><td id="119"><a href="#119">119</a></td></tr
><tr id="gr_svn41_120"

><td id="120"><a href="#120">120</a></td></tr
><tr id="gr_svn41_121"

><td id="121"><a href="#121">121</a></td></tr
><tr id="gr_svn41_122"

><td id="122"><a href="#122">122</a></td></tr
><tr id="gr_svn41_123"

><td id="123"><a href="#123">123</a></td></tr
><tr id="gr_svn41_124"

><td id="124"><a href="#124">124</a></td></tr
><tr id="gr_svn41_125"

><td id="125"><a href="#125">125</a></td></tr
><tr id="gr_svn41_126"

><td id="126"><a href="#126">126</a></td></tr
><tr id="gr_svn41_127"

><td id="127"><a href="#127">127</a></td></tr
><tr id="gr_svn41_128"

><td id="128"><a href="#128">128</a></td></tr
><tr id="gr_svn41_129"

><td id="129"><a href="#129">129</a></td></tr
><tr id="gr_svn41_130"

><td id="130"><a href="#130">130</a></td></tr
><tr id="gr_svn41_131"

><td id="131"><a href="#131">131</a></td></tr
><tr id="gr_svn41_132"

><td id="132"><a href="#132">132</a></td></tr
><tr id="gr_svn41_133"

><td id="133"><a href="#133">133</a></td></tr
><tr id="gr_svn41_134"

><td id="134"><a href="#134">134</a></td></tr
><tr id="gr_svn41_135"

><td id="135"><a href="#135">135</a></td></tr
><tr id="gr_svn41_136"

><td id="136"><a href="#136">136</a></td></tr
><tr id="gr_svn41_137"

><td id="137"><a href="#137">137</a></td></tr
><tr id="gr_svn41_138"

><td id="138"><a href="#138">138</a></td></tr
><tr id="gr_svn41_139"

><td id="139"><a href="#139">139</a></td></tr
><tr id="gr_svn41_140"

><td id="140"><a href="#140">140</a></td></tr
><tr id="gr_svn41_141"

><td id="141"><a href="#141">141</a></td></tr
><tr id="gr_svn41_142"

><td id="142"><a href="#142">142</a></td></tr
><tr id="gr_svn41_143"

><td id="143"><a href="#143">143</a></td></tr
><tr id="gr_svn41_144"

><td id="144"><a href="#144">144</a></td></tr
><tr id="gr_svn41_145"

><td id="145"><a href="#145">145</a></td></tr
><tr id="gr_svn41_146"

><td id="146"><a href="#146">146</a></td></tr
><tr id="gr_svn41_147"

><td id="147"><a href="#147">147</a></td></tr
><tr id="gr_svn41_148"

><td id="148"><a href="#148">148</a></td></tr
><tr id="gr_svn41_149"

><td id="149"><a href="#149">149</a></td></tr
><tr id="gr_svn41_150"

><td id="150"><a href="#150">150</a></td></tr
><tr id="gr_svn41_151"

><td id="151"><a href="#151">151</a></td></tr
><tr id="gr_svn41_152"

><td id="152"><a href="#152">152</a></td></tr
><tr id="gr_svn41_153"

><td id="153"><a href="#153">153</a></td></tr
><tr id="gr_svn41_154"

><td id="154"><a href="#154">154</a></td></tr
><tr id="gr_svn41_155"

><td id="155"><a href="#155">155</a></td></tr
><tr id="gr_svn41_156"

><td id="156"><a href="#156">156</a></td></tr
><tr id="gr_svn41_157"

><td id="157"><a href="#157">157</a></td></tr
><tr id="gr_svn41_158"

><td id="158"><a href="#158">158</a></td></tr
><tr id="gr_svn41_159"

><td id="159"><a href="#159">159</a></td></tr
><tr id="gr_svn41_160"

><td id="160"><a href="#160">160</a></td></tr
><tr id="gr_svn41_161"

><td id="161"><a href="#161">161</a></td></tr
><tr id="gr_svn41_162"

><td id="162"><a href="#162">162</a></td></tr
><tr id="gr_svn41_163"

><td id="163"><a href="#163">163</a></td></tr
><tr id="gr_svn41_164"

><td id="164"><a href="#164">164</a></td></tr
><tr id="gr_svn41_165"

><td id="165"><a href="#165">165</a></td></tr
><tr id="gr_svn41_166"

><td id="166"><a href="#166">166</a></td></tr
><tr id="gr_svn41_167"

><td id="167"><a href="#167">167</a></td></tr
><tr id="gr_svn41_168"

><td id="168"><a href="#168">168</a></td></tr
><tr id="gr_svn41_169"

><td id="169"><a href="#169">169</a></td></tr
><tr id="gr_svn41_170"

><td id="170"><a href="#170">170</a></td></tr
><tr id="gr_svn41_171"

><td id="171"><a href="#171">171</a></td></tr
><tr id="gr_svn41_172"

><td id="172"><a href="#172">172</a></td></tr
><tr id="gr_svn41_173"

><td id="173"><a href="#173">173</a></td></tr
><tr id="gr_svn41_174"

><td id="174"><a href="#174">174</a></td></tr
><tr id="gr_svn41_175"

><td id="175"><a href="#175">175</a></td></tr
><tr id="gr_svn41_176"

><td id="176"><a href="#176">176</a></td></tr
><tr id="gr_svn41_177"

><td id="177"><a href="#177">177</a></td></tr
><tr id="gr_svn41_178"

><td id="178"><a href="#178">178</a></td></tr
><tr id="gr_svn41_179"

><td id="179"><a href="#179">179</a></td></tr
><tr id="gr_svn41_180"

><td id="180"><a href="#180">180</a></td></tr
><tr id="gr_svn41_181"

><td id="181"><a href="#181">181</a></td></tr
><tr id="gr_svn41_182"

><td id="182"><a href="#182">182</a></td></tr
><tr id="gr_svn41_183"

><td id="183"><a href="#183">183</a></td></tr
><tr id="gr_svn41_184"

><td id="184"><a href="#184">184</a></td></tr
><tr id="gr_svn41_185"

><td id="185"><a href="#185">185</a></td></tr
><tr id="gr_svn41_186"

><td id="186"><a href="#186">186</a></td></tr
><tr id="gr_svn41_187"

><td id="187"><a href="#187">187</a></td></tr
><tr id="gr_svn41_188"

><td id="188"><a href="#188">188</a></td></tr
><tr id="gr_svn41_189"

><td id="189"><a href="#189">189</a></td></tr
><tr id="gr_svn41_190"

><td id="190"><a href="#190">190</a></td></tr
><tr id="gr_svn41_191"

><td id="191"><a href="#191">191</a></td></tr
><tr id="gr_svn41_192"

><td id="192"><a href="#192">192</a></td></tr
><tr id="gr_svn41_193"

><td id="193"><a href="#193">193</a></td></tr
><tr id="gr_svn41_194"

><td id="194"><a href="#194">194</a></td></tr
><tr id="gr_svn41_195"

><td id="195"><a href="#195">195</a></td></tr
><tr id="gr_svn41_196"

><td id="196"><a href="#196">196</a></td></tr
><tr id="gr_svn41_197"

><td id="197"><a href="#197">197</a></td></tr
><tr id="gr_svn41_198"

><td id="198"><a href="#198">198</a></td></tr
><tr id="gr_svn41_199"

><td id="199"><a href="#199">199</a></td></tr
><tr id="gr_svn41_200"

><td id="200"><a href="#200">200</a></td></tr
><tr id="gr_svn41_201"

><td id="201"><a href="#201">201</a></td></tr
><tr id="gr_svn41_202"

><td id="202"><a href="#202">202</a></td></tr
><tr id="gr_svn41_203"

><td id="203"><a href="#203">203</a></td></tr
><tr id="gr_svn41_204"

><td id="204"><a href="#204">204</a></td></tr
><tr id="gr_svn41_205"

><td id="205"><a href="#205">205</a></td></tr
><tr id="gr_svn41_206"

><td id="206"><a href="#206">206</a></td></tr
><tr id="gr_svn41_207"

><td id="207"><a href="#207">207</a></td></tr
><tr id="gr_svn41_208"

><td id="208"><a href="#208">208</a></td></tr
><tr id="gr_svn41_209"

><td id="209"><a href="#209">209</a></td></tr
><tr id="gr_svn41_210"

><td id="210"><a href="#210">210</a></td></tr
><tr id="gr_svn41_211"

><td id="211"><a href="#211">211</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn41_1

><td class="source">import logging, sys, os,\<br></td></tr
><tr
id=sl_svn41_2

><td class="source">       subprocess , random,\<br></td></tr
><tr
id=sl_svn41_3

><td class="source">       time, thread, math<br></td></tr
><tr
id=sl_svn41_4

><td class="source"><br></td></tr
><tr
id=sl_svn41_5

><td class="source">import Pyro.core, Pyro.naming<br></td></tr
><tr
id=sl_svn41_6

><td class="source">from ControlClass import  ControlClass<br></td></tr
><tr
id=sl_svn41_7

><td class="source"><br></td></tr
><tr
id=sl_svn41_8

><td class="source"><br></td></tr
><tr
id=sl_svn41_9

><td class="source">#Enable debugging/ send to stderr<br></td></tr
><tr
id=sl_svn41_10

><td class="source">logging.basicConfig(level=logging.INFO)<br></td></tr
><tr
id=sl_svn41_11

><td class="source"><br></td></tr
><tr
id=sl_svn41_12

><td class="source">nodeHandles = []<br></td></tr
><tr
id=sl_svn41_13

><td class="source">nodeStatus  = []<br></td></tr
><tr
id=sl_svn41_14

><td class="source"><br></td></tr
><tr
id=sl_svn41_15

><td class="source">class ChordControl:<br></td></tr
><tr
id=sl_svn41_16

><td class="source">    <br></td></tr
><tr
id=sl_svn41_17

><td class="source">    def __init__(self,clients,churn):<br></td></tr
><tr
id=sl_svn41_18

><td class="source">        self._portNumber = 4900<br></td></tr
><tr
id=sl_svn41_19

><td class="source">        self._basePort = 5000<br></td></tr
><tr
id=sl_svn41_20

><td class="source">        self._bootstrapPort = 5000<br></td></tr
><tr
id=sl_svn41_21

><td class="source">        self._n_clients = clients<br></td></tr
><tr
id=sl_svn41_22

><td class="source">        self._churn_rate = churn<br></td></tr
><tr
id=sl_svn41_23

><td class="source">        self._controlClassInstance = ControlClass(self)<br></td></tr
><tr
id=sl_svn41_24

><td class="source">        self._liveNodes = 0<br></td></tr
><tr
id=sl_svn41_25

><td class="source">        #Start control server that will hand-out bootstrap nodes<br></td></tr
><tr
id=sl_svn41_26

><td class="source">        thread.start_new_thread(self.controlServer,())<br></td></tr
><tr
id=sl_svn41_27

><td class="source">    <br></td></tr
><tr
id=sl_svn41_28

><td class="source">        #Create client nodes    <br></td></tr
><tr
id=sl_svn41_29

><td class="source">        self.createClients()<br></td></tr
><tr
id=sl_svn41_30

><td class="source">    <br></td></tr
><tr
id=sl_svn41_31

><td class="source">    def createClientProcess(self,portNumber,bootstrapPort):<br></td></tr
><tr
id=sl_svn41_32

><td class="source">        &quot;Spawn a new CHORD client process,\<br></td></tr
><tr
id=sl_svn41_33

><td class="source">        supplying it with a portto bind to&quot;<br></td></tr
><tr
id=sl_svn41_34

><td class="source">        time.sleep(0.2)<br></td></tr
><tr
id=sl_svn41_35

><td class="source">        logging.debug(&quot;Master Process:Creating new Chord client&quot;)<br></td></tr
><tr
id=sl_svn41_36

><td class="source">        subprocess.Popen([&quot;python&quot;,&quot;../Process/__init__.py&quot;,str(portNumber),str(bootstrapPort),str(self._churn_rate)])<br></td></tr
><tr
id=sl_svn41_37

><td class="source">        <br></td></tr
><tr
id=sl_svn41_38

><td class="source">    def getNodeHandles(self):<br></td></tr
><tr
id=sl_svn41_39

><td class="source">        &quot;Create CHORD clients with unique portNumber\<br></td></tr
><tr
id=sl_svn41_40

><td class="source">        and a bootstrap node&quot;    <br></td></tr
><tr
id=sl_svn41_41

><td class="source">        portNumber = self._basePort+1<br></td></tr
><tr
id=sl_svn41_42

><td class="source">        for client in range(self._n_clients):<br></td></tr
><tr
id=sl_svn41_43

><td class="source">            nodeHandles.append(self.getProxy(portNumber)) <br></td></tr
><tr
id=sl_svn41_44

><td class="source">            nodeStatus.append(True)<br></td></tr
><tr
id=sl_svn41_45

><td class="source">            self._liveNodes+=1<br></td></tr
><tr
id=sl_svn41_46

><td class="source">            portNumber = portNumber + 2<br></td></tr
><tr
id=sl_svn41_47

><td class="source">        return nodeHandles<br></td></tr
><tr
id=sl_svn41_48

><td class="source">    <br></td></tr
><tr
id=sl_svn41_49

><td class="source">    def createClients(self):<br></td></tr
><tr
id=sl_svn41_50

><td class="source">        &quot;Create CHORD clients with unique portNumber\<br></td></tr
><tr
id=sl_svn41_51

><td class="source">        and a bootstrap node&quot;    <br></td></tr
><tr
id=sl_svn41_52

><td class="source">        portNumber = self._basePort<br></td></tr
><tr
id=sl_svn41_53

><td class="source">        for client in range(self._n_clients):<br></td></tr
><tr
id=sl_svn41_54

><td class="source">            self.createClientProcess(portNumber,self._bootstrapPort)<br></td></tr
><tr
id=sl_svn41_55

><td class="source">            portNumber = portNumber + 2    <br></td></tr
><tr
id=sl_svn41_56

><td class="source">            if portNumber &gt;=5004:<br></td></tr
><tr
id=sl_svn41_57

><td class="source">                self._bootstrapPort = self._bootstrapPort + 2<br></td></tr
><tr
id=sl_svn41_58

><td class="source">    <br></td></tr
><tr
id=sl_svn41_59

><td class="source">        <br></td></tr
><tr
id=sl_svn41_60

><td class="source">        time.sleep(4)<br></td></tr
><tr
id=sl_svn41_61

><td class="source">    <br></td></tr
><tr
id=sl_svn41_62

><td class="source">        self.getNodeHandles()<br></td></tr
><tr
id=sl_svn41_63

><td class="source">        <br></td></tr
><tr
id=sl_svn41_64

><td class="source">    def isAlive(self,node):<br></td></tr
><tr
id=sl_svn41_65

><td class="source">        try: <br></td></tr
><tr
id=sl_svn41_66

><td class="source">            return node.isAlive()<br></td></tr
><tr
id=sl_svn41_67

><td class="source">        except:<br></td></tr
><tr
id=sl_svn41_68

><td class="source">            return False<br></td></tr
><tr
id=sl_svn41_69

><td class="source">        <br></td></tr
><tr
id=sl_svn41_70

><td class="source">    <br></td></tr
><tr
id=sl_svn41_71

><td class="source">    def getProxy(self,portNumber):<br></td></tr
><tr
id=sl_svn41_72

><td class="source">        &quot;Given the port in the name service,\<br></td></tr
><tr
id=sl_svn41_73

><td class="source">        returns a proxy of the remote object&quot;<br></td></tr
><tr
id=sl_svn41_74

><td class="source">        proxy = Pyro.core.getProxyForURI(&quot;PYRONAME://{0}&quot;.format(portNumber))<br></td></tr
><tr
id=sl_svn41_75

><td class="source">        return proxy   <br></td></tr
><tr
id=sl_svn41_76

><td class="source">              <br></td></tr
><tr
id=sl_svn41_77

><td class="source">    def searchFile(self,pos,file):      <br></td></tr
><tr
id=sl_svn41_78

><td class="source">        node,steps = nodeHandles[pos].searchFile(file)<br></td></tr
><tr
id=sl_svn41_79

><td class="source">        print &quot;Master Process:File {0} found in node {1} in {2} steps&quot;.format(file,node,steps)<br></td></tr
><tr
id=sl_svn41_80

><td class="source">        <br></td></tr
><tr
id=sl_svn41_81

><td class="source">        <br></td></tr
><tr
id=sl_svn41_82

><td class="source">    def controlServer(self):<br></td></tr
><tr
id=sl_svn41_83

><td class="source">        &quot;The only purpose of this server is to\<br></td></tr
><tr
id=sl_svn41_84

><td class="source">        hand-out bootstrap ports, to nodes that\<br></td></tr
><tr
id=sl_svn41_85

><td class="source">        want to rejoin the chord network,after\<br></td></tr
><tr
id=sl_svn41_86

><td class="source">        a failure&quot;<br></td></tr
><tr
id=sl_svn41_87

><td class="source">        Pyro.core.initServer()<br></td></tr
><tr
id=sl_svn41_88

><td class="source">        ns=Pyro.naming.NameServerLocator().getNS()<br></td></tr
><tr
id=sl_svn41_89

><td class="source">        self._cdaemon=Pyro.core.Daemon()<br></td></tr
><tr
id=sl_svn41_90

><td class="source">        self._cdaemon.useNameServer(ns)<br></td></tr
><tr
id=sl_svn41_91

><td class="source">        <br></td></tr
><tr
id=sl_svn41_92

><td class="source">        uri=self._cdaemon.connect(self._controlClassInstance,str(self._portNumber))<br></td></tr
><tr
id=sl_svn41_93

><td class="source">        <br></td></tr
><tr
id=sl_svn41_94

><td class="source">        logging.debug(&quot;Master Process: Listening for Control messages on {0}&quot;.format(self._cdaemon.port))<br></td></tr
><tr
id=sl_svn41_95

><td class="source">        <br></td></tr
><tr
id=sl_svn41_96

><td class="source">        self._cdaemon.requestLoop()<br></td></tr
><tr
id=sl_svn41_97

><td class="source">        <br></td></tr
><tr
id=sl_svn41_98

><td class="source">    def insertFiles(self,fileInserts):<br></td></tr
><tr
id=sl_svn41_99

><td class="source">        print &quot;Master Process:Master Process:Inserting files into Chord network.&quot;<br></td></tr
><tr
id=sl_svn41_100

><td class="source">        for i in range(fileInserts):<br></td></tr
><tr
id=sl_svn41_101

><td class="source">            for index,node in enumerate(nodeHandles):<br></td></tr
><tr
id=sl_svn41_102

><td class="source">                if nodeStatus[index]: # and node.isAlive():<br></td></tr
><tr
id=sl_svn41_103

><td class="source">                    node.insertFile(&quot;files/foo{0}&quot;.format(i))<br></td></tr
><tr
id=sl_svn41_104

><td class="source">                    cnt=0<br></td></tr
><tr
id=sl_svn41_105

><td class="source">                    for j in nodeStatus:<br></td></tr
><tr
id=sl_svn41_106

><td class="source">                        if j:<br></td></tr
><tr
id=sl_svn41_107

><td class="source">                            cnt+=1<br></td></tr
><tr
id=sl_svn41_108

><td class="source">                    if self._churn_rate &gt; 0:<br></td></tr
><tr
id=sl_svn41_109

><td class="source">                        print &quot;Number of live nodes {0}&quot;.format(cnt)<br></td></tr
><tr
id=sl_svn41_110

><td class="source">                    break<br></td></tr
><tr
id=sl_svn41_111

><td class="source">                <br></td></tr
><tr
id=sl_svn41_112

><td class="source">            time.sleep(0.05);<br></td></tr
><tr
id=sl_svn41_113

><td class="source">        print &quot;Master Process: Done inserting&quot;         <br></td></tr
><tr
id=sl_svn41_114

><td class="source">        <br></td></tr
><tr
id=sl_svn41_115

><td class="source">    def searchFiles(self,fileSearches):<br></td></tr
><tr
id=sl_svn41_116

><td class="source">        totalSteps = 0.<br></td></tr
><tr
id=sl_svn41_117

><td class="source">        searchFails = 0<br></td></tr
><tr
id=sl_svn41_118

><td class="source">        print &quot;Master Process:Searching for files...&quot;<br></td></tr
><tr
id=sl_svn41_119

><td class="source">        for file in range(fileSearches):<br></td></tr
><tr
id=sl_svn41_120

><td class="source">            retries = 0<br></td></tr
><tr
id=sl_svn41_121

><td class="source">            searchStatus = False<br></td></tr
><tr
id=sl_svn41_122

><td class="source">            <br></td></tr
><tr
id=sl_svn41_123

><td class="source">            if self._churn_rate &gt; 0:<br></td></tr
><tr
id=sl_svn41_124

><td class="source">                delay = math.ceil(random.expovariate(1)*3)<br></td></tr
><tr
id=sl_svn41_125

><td class="source">                time.sleep(delay)<br></td></tr
><tr
id=sl_svn41_126

><td class="source">            <br></td></tr
><tr
id=sl_svn41_127

><td class="source">            print &quot;Searching for file foo{0}:&quot;.format(file)            <br></td></tr
><tr
id=sl_svn41_128

><td class="source">            <br></td></tr
><tr
id=sl_svn41_129

><td class="source">            # Randomly select one node to search the file<br></td></tr
><tr
id=sl_svn41_130

><td class="source">            while retries &lt; 5:<br></td></tr
><tr
id=sl_svn41_131

><td class="source">                index = random.randint(0,self._n_clients-1)<br></td></tr
><tr
id=sl_svn41_132

><td class="source">                if nodeStatus[index]: # nodeHandles[index].isAlive():<br></td></tr
><tr
id=sl_svn41_133

><td class="source">                    print &quot;Master process: Searching for file foo{0} from node {1}&quot;.format(file,nodeHandles[index].getKey())<br></td></tr
><tr
id=sl_svn41_134

><td class="source">                    try:<br></td></tr
><tr
id=sl_svn41_135

><td class="source">                        (node,steps)= nodeHandles[index].searchFile(&quot;foo{0}&quot;.format(file))<br></td></tr
><tr
id=sl_svn41_136

><td class="source">                        searchStatus = True<br></td></tr
><tr
id=sl_svn41_137

><td class="source">                    except:<br></td></tr
><tr
id=sl_svn41_138

><td class="source">                        searchStatus = False<br></td></tr
><tr
id=sl_svn41_139

><td class="source">                    break<br></td></tr
><tr
id=sl_svn41_140

><td class="source">                retries += 1<br></td></tr
><tr
id=sl_svn41_141

><td class="source">                    <br></td></tr
><tr
id=sl_svn41_142

><td class="source">            if not searchStatus:<br></td></tr
><tr
id=sl_svn41_143

><td class="source">                fileSearches -=1<br></td></tr
><tr
id=sl_svn41_144

><td class="source">                continue<br></td></tr
><tr
id=sl_svn41_145

><td class="source">            <br></td></tr
><tr
id=sl_svn41_146

><td class="source">            if node ==None: <br></td></tr
><tr
id=sl_svn41_147

><td class="source">                searchFails += 1<br></td></tr
><tr
id=sl_svn41_148

><td class="source">            totalSteps = totalSteps + steps<br></td></tr
><tr
id=sl_svn41_149

><td class="source">            <br></td></tr
><tr
id=sl_svn41_150

><td class="source">        print &quot;Master Process: Total number of failed searches: {0} out of {1} ({2}% failure rate)&quot;.format(searchFails,fileSearches,float(searchFails)/fileSearches)<br></td></tr
><tr
id=sl_svn41_151

><td class="source">        print &quot;Master Process: Total number of steps: {0} ({1} steps on average)&quot;.format(totalSteps,totalSteps/fileSearches)<br></td></tr
><tr
id=sl_svn41_152

><td class="source">        <br></td></tr
><tr
id=sl_svn41_153

><td class="source">    def getBootstrapNode(self):<br></td></tr
><tr
id=sl_svn41_154

><td class="source">        for node in nodeHandles:<br></td></tr
><tr
id=sl_svn41_155

><td class="source">            if node.isAlive():<br></td></tr
><tr
id=sl_svn41_156

><td class="source">                return node.getPort()<br></td></tr
><tr
id=sl_svn41_157

><td class="source">        <br></td></tr
><tr
id=sl_svn41_158

><td class="source">        logging.error(&quot;No node is alive in the Network&quot;)<br></td></tr
><tr
id=sl_svn41_159

><td class="source">        <br></td></tr
><tr
id=sl_svn41_160

><td class="source">    def notifyControl(self,port,status):<br></td></tr
><tr
id=sl_svn41_161

><td class="source">        pos = (port -  self._basePort) / 2<br></td></tr
><tr
id=sl_svn41_162

><td class="source">        if status==False:<br></td></tr
><tr
id=sl_svn41_163

><td class="source">            if self._liveNodes &lt;= math.ceil((1-self._churn_rate)*self._n_clients):<br></td></tr
><tr
id=sl_svn41_164

><td class="source">                return False<br></td></tr
><tr
id=sl_svn41_165

><td class="source">            <br></td></tr
><tr
id=sl_svn41_166

><td class="source">        if status:<br></td></tr
><tr
id=sl_svn41_167

><td class="source">            self._liveNodes+=1<br></td></tr
><tr
id=sl_svn41_168

><td class="source">        else:<br></td></tr
><tr
id=sl_svn41_169

><td class="source">            self._liveNodes-=1<br></td></tr
><tr
id=sl_svn41_170

><td class="source">            <br></td></tr
><tr
id=sl_svn41_171

><td class="source">        nodeStatus[pos] = status<br></td></tr
><tr
id=sl_svn41_172

><td class="source">        return True<br></td></tr
><tr
id=sl_svn41_173

><td class="source">        <br></td></tr
><tr
id=sl_svn41_174

><td class="source">        <br></td></tr
><tr
id=sl_svn41_175

><td class="source">        <br></td></tr
><tr
id=sl_svn41_176

><td class="source">def main():<br></td></tr
><tr
id=sl_svn41_177

><td class="source">    <br></td></tr
><tr
id=sl_svn41_178

><td class="source">    # The number of chord processes should be given<br></td></tr
><tr
id=sl_svn41_179

><td class="source">    # as a command line argument        <br></td></tr
><tr
id=sl_svn41_180

><td class="source">    if len(sys.argv) !=3:<br></td></tr
><tr
id=sl_svn41_181

><td class="source">        sys.stderr.write(&quot;Usage: chordControl PROCS_NUMBER CHURN_RATE&quot;)<br></td></tr
><tr
id=sl_svn41_182

><td class="source">        exit()<br></td></tr
><tr
id=sl_svn41_183

><td class="source">    numberOfClients = int(sys.argv[1])<br></td></tr
><tr
id=sl_svn41_184

><td class="source">    churn = float(sys.argv[2])<br></td></tr
><tr
id=sl_svn41_185

><td class="source">    <br></td></tr
><tr
id=sl_svn41_186

><td class="source">    c = ChordControl(numberOfClients,churn)<br></td></tr
><tr
id=sl_svn41_187

><td class="source">    <br></td></tr
><tr
id=sl_svn41_188

><td class="source">    #Wait for user, in order to proceed<br></td></tr
><tr
id=sl_svn41_189

><td class="source">    sys.stdin.readline(1)<br></td></tr
><tr
id=sl_svn41_190

><td class="source">    <br></td></tr
><tr
id=sl_svn41_191

><td class="source">    fileInserts = 1000<br></td></tr
><tr
id=sl_svn41_192

><td class="source">    fileSearches = 1000<br></td></tr
><tr
id=sl_svn41_193

><td class="source">    <br></td></tr
><tr
id=sl_svn41_194

><td class="source">    # Insert files in ring<br></td></tr
><tr
id=sl_svn41_195

><td class="source">    c.insertFiles(fileInserts)<br></td></tr
><tr
id=sl_svn41_196

><td class="source">    <br></td></tr
><tr
id=sl_svn41_197

><td class="source">    # Wait until user input given<br></td></tr
><tr
id=sl_svn41_198

><td class="source">    sys.stdin.readline(1)<br></td></tr
><tr
id=sl_svn41_199

><td class="source"><br></td></tr
><tr
id=sl_svn41_200

><td class="source">    c.searchFiles(fileSearches)<br></td></tr
><tr
id=sl_svn41_201

><td class="source">    <br></td></tr
><tr
id=sl_svn41_202

><td class="source">    <br></td></tr
><tr
id=sl_svn41_203

><td class="source">if  __name__ == &quot;__main__&quot;:<br></td></tr
><tr
id=sl_svn41_204

><td class="source">    main()<br></td></tr
><tr
id=sl_svn41_205

><td class="source"><br></td></tr
><tr
id=sl_svn41_206

><td class="source">    <br></td></tr
><tr
id=sl_svn41_207

><td class="source"><br></td></tr
><tr
id=sl_svn41_208

><td class="source">    <br></td></tr
><tr
id=sl_svn41_209

><td class="source">    <br></td></tr
><tr
id=sl_svn41_210

><td class="source"><br></td></tr
><tr
id=sl_svn41_211

><td class="source">    <br></td></tr
></table></pre>
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
</td>
</tr></table>

 
<script type="text/javascript">
 var lineNumUnderMouse = -1;
 
 function gutterOver(num) {
 gutterOut();
 var newTR = document.getElementById('gr_svn41_' + num);
 if (newTR) {
 newTR.className = 'undermouse';
 }
 lineNumUnderMouse = num;
 }
 function gutterOut() {
 if (lineNumUnderMouse != -1) {
 var oldTR = document.getElementById(
 'gr_svn41_' + lineNumUnderMouse);
 if (oldTR) {
 oldTR.className = '';
 }
 lineNumUnderMouse = -1;
 }
 }
 var numsGenState = {table_base_id: 'nums_table_'};
 var srcGenState = {table_base_id: 'src_table_'};
 var alignerRunning = false;
 var startOver = false;
 function setLineNumberHeights() {
 if (alignerRunning) {
 startOver = true;
 return;
 }
 numsGenState.chunk_id = 0;
 numsGenState.table = document.getElementById('nums_table_0');
 numsGenState.row_num = 0;
 if (!numsGenState.table) {
 return; // Silently exit if no file is present.
 }
 srcGenState.chunk_id = 0;
 srcGenState.table = document.getElementById('src_table_0');
 srcGenState.row_num = 0;
 alignerRunning = true;
 continueToSetLineNumberHeights();
 }
 function rowGenerator(genState) {
 if (genState.row_num < genState.table.rows.length) {
 var currentRow = genState.table.rows[genState.row_num];
 genState.row_num++;
 return currentRow;
 }
 var newTable = document.getElementById(
 genState.table_base_id + (genState.chunk_id + 1));
 if (newTable) {
 genState.chunk_id++;
 genState.row_num = 0;
 genState.table = newTable;
 return genState.table.rows[0];
 }
 return null;
 }
 var MAX_ROWS_PER_PASS = 1000;
 function continueToSetLineNumberHeights() {
 var rowsInThisPass = 0;
 var numRow = 1;
 var srcRow = 1;
 while (numRow && srcRow && rowsInThisPass < MAX_ROWS_PER_PASS) {
 numRow = rowGenerator(numsGenState);
 srcRow = rowGenerator(srcGenState);
 rowsInThisPass++;
 if (numRow && srcRow) {
 if (numRow.offsetHeight != srcRow.offsetHeight) {
 numRow.firstChild.style.height = srcRow.offsetHeight + 'px';
 }
 }
 }
 if (rowsInThisPass >= MAX_ROWS_PER_PASS) {
 setTimeout(continueToSetLineNumberHeights, 10);
 } else {
 alignerRunning = false;
 if (startOver) {
 startOver = false;
 setTimeout(setLineNumberHeights, 500);
 }
 }
 }
 function initLineNumberHeights() {
 // Do 2 complete passes, because there can be races
 // between this code and prettify.
 startOver = true;
 setTimeout(setLineNumberHeights, 250);
 window.onresize = setLineNumberHeights;
 }
 initLineNumberHeights();
</script>

 
 
 <div id="log">
 <div style="text-align:right">
 <a class="ifCollapse" href="#" onclick="_toggleMeta(this); return false">Show details</a>
 <a class="ifExpand" href="#" onclick="_toggleMeta(this); return false">Hide details</a>
 </div>
 <div class="ifExpand">
 
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="changelog">
 <p>Change log</p>
 <div>
 <a href="/p/chordimplementation/source/detail?spec=svn41&amp;r=41">r41</a>
 by nassosantoniou
 on Jun 11, 2010
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=41&amp;format=side&amp;path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old_path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old=40">Diff</a>
 </div>
 <pre>[No log message]</pre>
 </div>
 
 
 
 
 
 
 <script type="text/javascript">
 var detail_url = '/p/chordimplementation/source/detail?r=41&spec=svn41';
 var publish_url = '/p/chordimplementation/source/detail?r=41&spec=svn41#publish';
 // describe the paths of this revision in javascript.
 var changed_paths = [];
 var changed_urls = [];
 
 changed_paths.push('/trunk/ChordImplementation/src/ChordControl/ControlClass.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/ControlClass.py?r\x3d41\x26spec\x3dsvn41');
 
 
 changed_paths.push('/trunk/ChordImplementation/src/ChordControl/__init__.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/__init__.py?r\x3d41\x26spec\x3dsvn41');
 
 var selected_path = '/trunk/ChordImplementation/src/ChordControl/__init__.py';
 
 
 changed_paths.push('/trunk/ChordImplementation/src/Process/ChordProcessRecord.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ChordProcessRecord.py?r\x3d41\x26spec\x3dsvn41');
 
 
 changed_paths.push('/trunk/ChordImplementation/src/Process/ControlClass.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ControlClass.py?r\x3d41\x26spec\x3dsvn41');
 
 
 changed_paths.push('/trunk/ChordImplementation/src/Process/__init__.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/__init__.py?r\x3d41\x26spec\x3dsvn41');
 
 
 function getCurrentPageIndex() {
 for (var i = 0; i < changed_paths.length; i++) {
 if (selected_path == changed_paths[i]) {
 return i;
 }
 }
 }
 function getNextPage() {
 var i = getCurrentPageIndex();
 if (i < changed_paths.length - 1) {
 return changed_urls[i + 1];
 }
 return null;
 }
 function getPreviousPage() {
 var i = getCurrentPageIndex();
 if (i > 0) {
 return changed_urls[i - 1];
 }
 return null;
 }
 function gotoNextPage() {
 var page = getNextPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoPreviousPage() {
 var page = getPreviousPage();
 if (!page) {
 page = detail_url;
 }
 window.location = page;
 }
 function gotoDetailPage() {
 window.location = detail_url;
 }
 function gotoPublishPage() {
 window.location = publish_url;
 }
</script>

 
 <style type="text/css">
 #review_nav {
 border-top: 3px solid white;
 padding-top: 6px;
 margin-top: 1em;
 }
 #review_nav td {
 vertical-align: middle;
 }
 #review_nav select {
 margin: .5em 0;
 }
 </style>
 <div id="review_nav">
 <table><tr><td>Go to:&nbsp;</td><td>
 <select name="files_in_rev" onchange="window.location=this.value">
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/ControlClass.py?r=41&amp;spec=svn41"
 
 >...src/ChordControl/ControlClass.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/ChordControl/__init__.py?r=41&amp;spec=svn41"
 selected="selected"
 >...ion/src/ChordControl/__init__.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ChordProcessRecord.py?r=41&amp;spec=svn41"
 
 >...rc/Process/ChordProcessRecord.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ControlClass.py?r=41&amp;spec=svn41"
 
 >...tion/src/Process/ControlClass.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/__init__.py?r=41&amp;spec=svn41"
 
 >...entation/src/Process/__init__.py</option>
 
 </select>
 </td></tr></table>
 
 
 



 
 </div>
 
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="older_bubble">
 <p>Older revisions</p>
 
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/chordimplementation/source/detail?spec=svn41&r=40">r40</a>
 by nassosantoniou
 on Jun 6, 2010
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=40&amp;format=side&amp;path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old_path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old=37">Diff</a>
 <br>
 <pre class="ifOpened">[No log message]</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/chordimplementation/source/detail?spec=svn41&r=37">r37</a>
 by nassosantoniou
 on May 22, 2010
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=37&amp;format=side&amp;path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old_path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old=36">Diff</a>
 <br>
 <pre class="ifOpened">[No log message]</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/chordimplementation/source/detail?spec=svn41&r=36">r36</a>
 by nassosantoniou
 on May 22, 2010
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=36&amp;format=side&amp;path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old_path=/trunk/ChordImplementation/src/ChordControl/__init__.py&amp;old=31">Diff</a>
 <br>
 <pre class="ifOpened">[No log message]</pre>
 </div>
 
 
 <a href="/p/chordimplementation/source/list?path=/trunk/ChordImplementation/src/ChordControl/__init__.py&start=41">All revisions of this file</a>
 </div>
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 
 <div class="pmeta_bubble_bg" style="border:1px solid white">
 <div class="round4"></div>
 <div class="round2"></div>
 <div class="round1"></div>
 <div class="box-inner">
 <div id="fileinfo_bubble">
 <p>File info</p>
 
 <div>Size: 6925 bytes,
 211 lines</div>
 
 <div><a href="//chordimplementation.googlecode.com/svn/trunk/ChordImplementation/src/ChordControl/__init__.py">View raw file</a></div>
 </div>
 
 </div>
 <div class="round1"></div>
 <div class="round2"></div>
 <div class="round4"></div>
 </div>
 </div>
 </div>


</div>

</div>
</div>

<script src="https://ssl.gstatic.com/codesite/ph/13714586478408612229/js/prettify/prettify.js"></script>
<script type="text/javascript">prettyPrint();</script>


<script src="https://ssl.gstatic.com/codesite/ph/13714586478408612229/js/source_file_scripts.js"></script>

 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13714586478408612229/js/kibbles.js"></script>
 <script type="text/javascript">
 var lastStop = null;
 var initialized = false;
 
 function updateCursor(next, prev) {
 if (prev && prev.element) {
 prev.element.className = 'cursor_stop cursor_hidden';
 }
 if (next && next.element) {
 next.element.className = 'cursor_stop cursor';
 lastStop = next.index;
 }
 }
 
 function pubRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftRevealed(data) {
 updateCursorForCell(data.cellId, 'cursor_stop cursor_hidden');
 if (initialized) {
 reloadCursors();
 }
 }
 
 function draftDestroyed(data) {
 updateCursorForCell(data.cellId, 'nocursor');
 if (initialized) {
 reloadCursors();
 }
 }
 function reloadCursors() {
 kibbles.skipper.reset();
 loadCursors();
 if (lastStop != null) {
 kibbles.skipper.setCurrentStop(lastStop);
 }
 }
 // possibly the simplest way to insert any newly added comments
 // is to update the class of the corresponding cursor row,
 // then refresh the entire list of rows.
 function updateCursorForCell(cellId, className) {
 var cell = document.getElementById(cellId);
 // we have to go two rows back to find the cursor location
 var row = getPreviousElement(cell.parentNode);
 row.className = className;
 }
 // returns the previous element, ignores text nodes.
 function getPreviousElement(e) {
 var element = e.previousSibling;
 if (element.nodeType == 3) {
 element = element.previousSibling;
 }
 if (element && element.tagName) {
 return element;
 }
 }
 function loadCursors() {
 // register our elements with skipper
 var elements = CR_getElements('*', 'cursor_stop');
 var len = elements.length;
 for (var i = 0; i < len; i++) {
 var element = elements[i]; 
 element.className = 'cursor_stop cursor_hidden';
 kibbles.skipper.append(element);
 }
 }
 function toggleComments() {
 CR_toggleCommentDisplay();
 reloadCursors();
 }
 function keysOnLoadHandler() {
 // setup skipper
 kibbles.skipper.addStopListener(
 kibbles.skipper.LISTENER_TYPE.PRE, updateCursor);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_top', 50);
 // Set the 'offset' option to return the middle of the client area
 // an option can be a static value, or a callback
 kibbles.skipper.setOption('padding_bottom', 100);
 // Register our keys
 kibbles.skipper.addFwdKey("n");
 kibbles.skipper.addRevKey("p");
 kibbles.keys.addKeyPressListener(
 'u', function() { window.location = detail_url; });
 kibbles.keys.addKeyPressListener(
 'r', function() { window.location = detail_url + '#publish'; });
 
 kibbles.keys.addKeyPressListener('j', gotoNextPage);
 kibbles.keys.addKeyPressListener('k', gotoPreviousPage);
 
 
 }
 </script>
<script src="https://ssl.gstatic.com/codesite/ph/13714586478408612229/js/code_review_scripts.js"></script>
<script type="text/javascript">
 function showPublishInstructions() {
 var element = document.getElementById('review_instr');
 if (element) {
 element.className = 'opened';
 }
 }
 var codereviews;
 function revsOnLoadHandler() {
 // register our source container with the commenting code
 var paths = {'svn41': '/trunk/ChordImplementation/src/ChordControl/__init__.py'}
 codereviews = CR_controller.setup(
 {"projectHomeUrl":"/p/chordimplementation","loggedInUserEmail":"ethan.wjj@gmail.com","token":"58PYcNO9J8jdcRuj5DsCyfy4jKw:1366668602971","domainName":null,"profileUrl":"/u/115244174812975043353/","projectName":"chordimplementation","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/13714586478408612229","relativeBaseUrl":"","assetHostPath":"https://ssl.gstatic.com/codesite/ph"}, '', 'svn41', paths,
 CR_BrowseIntegrationFactory);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, showPublishInstructions);
 
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_PUB_PLATE, pubRevealed);
 codereviews.registerActivityListener(CR_ActivityType.REVEAL_DRAFT_PLATE, draftRevealed);
 codereviews.registerActivityListener(CR_ActivityType.DISCARD_DRAFT_COMMENT, draftDestroyed);
 
 
 
 
 
 
 
 var initialized = true;
 reloadCursors();
 }
 window.onload = function() {keysOnLoadHandler(); revsOnLoadHandler();};

</script>
<script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13714586478408612229/js/dit_scripts.js"></script>

 
 
 
 <script type="text/javascript" src="https://ssl.gstatic.com/codesite/ph/13714586478408612229/js/ph_core.js"></script>
 
 
 
 
</div> 

<div id="footer" dir="ltr">
 <div class="text">
 <a href="/projecthosting/terms.html">Terms</a> -
 <a href="http://www.google.com/privacy.html">Privacy</a> -
 <a href="/p/support/">Project Hosting Help</a>
 </div>
</div>
 <div class="hostedBy" style="margin-top: -20px;">
 <span style="vertical-align: top;">Powered by <a href="http://code.google.com/projecthosting/">Google Project Hosting</a></span>
 </div>

 
 


 
 </body>
</html>

