



<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" >
 <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" >
 
 <meta name="ROBOTS" content="NOARCHIVE">
 
 <link rel="icon" type="image/vnd.microsoft.icon" href="https://ssl.gstatic.com/codesite/ph/images/phosting.ico">
 
 
 <script type="text/javascript">
 
 
 
 
 var codesite_token = "hsWkZbmZwW-OF1_Kq8EigbCaddk:1366668725836";
 
 
 var CS_env = {"projectName":"chordimplementation","loggedInUserEmail":"ethan.wjj@gmail.com","profileUrl":"/u/115244174812975043353/","assetHostPath":"https://ssl.gstatic.com/codesite/ph","token":"hsWkZbmZwW-OF1_Kq8EigbCaddk:1366668725836","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/13714586478408612229","projectHomeUrl":"/p/chordimplementation","relativeBaseUrl":"","domainName":null};
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
 | <a href="https://www.google.com/accounts/Logout?continue=https%3A%2F%2Fcode.google.com%2Fp%2Fchordimplementation%2Fsource%2Fbrowse%2Ftrunk%2FChordImplementation%2Fsrc%2FProcess%2F__init__.py" 
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
 <span id="crumb_links" class="ifClosed"><a href="/p/chordimplementation/source/browse/trunk/">trunk</a><span class="sp">/&nbsp;</span><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/">ChordImplementation</a><span class="sp">/&nbsp;</span><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/">src</a><span class="sp">/&nbsp;</span><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/">Process</a><span class="sp">/&nbsp;</span>__init__.py</span>
 
 


 </td>
 
 
 <td nowrap="nowrap" width="33%" align="center">
 <a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/__init__.py?edit=1"
 ><img src="https://ssl.gstatic.com/codesite/ph/images/pencil-y14.png"
 class="edit_icon">Edit file</a>
 </td>
 
 
 <td nowrap="nowrap" width="33%" align="right">
 <table cellpadding="0" cellspacing="0" style="font-size: 100%"><tr>
 
 
 <td class="flipper">
 <ul class="leftside">
 
 <li><a href="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/__init__.py?r=40" title="Previous">&lsaquo;r40</a></li>
 
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
><tr id="gr_svn41_212"

><td id="212"><a href="#212">212</a></td></tr
><tr id="gr_svn41_213"

><td id="213"><a href="#213">213</a></td></tr
><tr id="gr_svn41_214"

><td id="214"><a href="#214">214</a></td></tr
><tr id="gr_svn41_215"

><td id="215"><a href="#215">215</a></td></tr
><tr id="gr_svn41_216"

><td id="216"><a href="#216">216</a></td></tr
><tr id="gr_svn41_217"

><td id="217"><a href="#217">217</a></td></tr
><tr id="gr_svn41_218"

><td id="218"><a href="#218">218</a></td></tr
><tr id="gr_svn41_219"

><td id="219"><a href="#219">219</a></td></tr
><tr id="gr_svn41_220"

><td id="220"><a href="#220">220</a></td></tr
><tr id="gr_svn41_221"

><td id="221"><a href="#221">221</a></td></tr
><tr id="gr_svn41_222"

><td id="222"><a href="#222">222</a></td></tr
><tr id="gr_svn41_223"

><td id="223"><a href="#223">223</a></td></tr
><tr id="gr_svn41_224"

><td id="224"><a href="#224">224</a></td></tr
><tr id="gr_svn41_225"

><td id="225"><a href="#225">225</a></td></tr
><tr id="gr_svn41_226"

><td id="226"><a href="#226">226</a></td></tr
><tr id="gr_svn41_227"

><td id="227"><a href="#227">227</a></td></tr
><tr id="gr_svn41_228"

><td id="228"><a href="#228">228</a></td></tr
><tr id="gr_svn41_229"

><td id="229"><a href="#229">229</a></td></tr
><tr id="gr_svn41_230"

><td id="230"><a href="#230">230</a></td></tr
><tr id="gr_svn41_231"

><td id="231"><a href="#231">231</a></td></tr
><tr id="gr_svn41_232"

><td id="232"><a href="#232">232</a></td></tr
><tr id="gr_svn41_233"

><td id="233"><a href="#233">233</a></td></tr
><tr id="gr_svn41_234"

><td id="234"><a href="#234">234</a></td></tr
><tr id="gr_svn41_235"

><td id="235"><a href="#235">235</a></td></tr
><tr id="gr_svn41_236"

><td id="236"><a href="#236">236</a></td></tr
><tr id="gr_svn41_237"

><td id="237"><a href="#237">237</a></td></tr
><tr id="gr_svn41_238"

><td id="238"><a href="#238">238</a></td></tr
><tr id="gr_svn41_239"

><td id="239"><a href="#239">239</a></td></tr
><tr id="gr_svn41_240"

><td id="240"><a href="#240">240</a></td></tr
><tr id="gr_svn41_241"

><td id="241"><a href="#241">241</a></td></tr
><tr id="gr_svn41_242"

><td id="242"><a href="#242">242</a></td></tr
><tr id="gr_svn41_243"

><td id="243"><a href="#243">243</a></td></tr
><tr id="gr_svn41_244"

><td id="244"><a href="#244">244</a></td></tr
><tr id="gr_svn41_245"

><td id="245"><a href="#245">245</a></td></tr
><tr id="gr_svn41_246"

><td id="246"><a href="#246">246</a></td></tr
><tr id="gr_svn41_247"

><td id="247"><a href="#247">247</a></td></tr
><tr id="gr_svn41_248"

><td id="248"><a href="#248">248</a></td></tr
><tr id="gr_svn41_249"

><td id="249"><a href="#249">249</a></td></tr
><tr id="gr_svn41_250"

><td id="250"><a href="#250">250</a></td></tr
><tr id="gr_svn41_251"

><td id="251"><a href="#251">251</a></td></tr
><tr id="gr_svn41_252"

><td id="252"><a href="#252">252</a></td></tr
><tr id="gr_svn41_253"

><td id="253"><a href="#253">253</a></td></tr
><tr id="gr_svn41_254"

><td id="254"><a href="#254">254</a></td></tr
><tr id="gr_svn41_255"

><td id="255"><a href="#255">255</a></td></tr
><tr id="gr_svn41_256"

><td id="256"><a href="#256">256</a></td></tr
><tr id="gr_svn41_257"

><td id="257"><a href="#257">257</a></td></tr
><tr id="gr_svn41_258"

><td id="258"><a href="#258">258</a></td></tr
><tr id="gr_svn41_259"

><td id="259"><a href="#259">259</a></td></tr
><tr id="gr_svn41_260"

><td id="260"><a href="#260">260</a></td></tr
><tr id="gr_svn41_261"

><td id="261"><a href="#261">261</a></td></tr
><tr id="gr_svn41_262"

><td id="262"><a href="#262">262</a></td></tr
><tr id="gr_svn41_263"

><td id="263"><a href="#263">263</a></td></tr
><tr id="gr_svn41_264"

><td id="264"><a href="#264">264</a></td></tr
><tr id="gr_svn41_265"

><td id="265"><a href="#265">265</a></td></tr
><tr id="gr_svn41_266"

><td id="266"><a href="#266">266</a></td></tr
><tr id="gr_svn41_267"

><td id="267"><a href="#267">267</a></td></tr
><tr id="gr_svn41_268"

><td id="268"><a href="#268">268</a></td></tr
><tr id="gr_svn41_269"

><td id="269"><a href="#269">269</a></td></tr
><tr id="gr_svn41_270"

><td id="270"><a href="#270">270</a></td></tr
><tr id="gr_svn41_271"

><td id="271"><a href="#271">271</a></td></tr
><tr id="gr_svn41_272"

><td id="272"><a href="#272">272</a></td></tr
><tr id="gr_svn41_273"

><td id="273"><a href="#273">273</a></td></tr
><tr id="gr_svn41_274"

><td id="274"><a href="#274">274</a></td></tr
><tr id="gr_svn41_275"

><td id="275"><a href="#275">275</a></td></tr
><tr id="gr_svn41_276"

><td id="276"><a href="#276">276</a></td></tr
><tr id="gr_svn41_277"

><td id="277"><a href="#277">277</a></td></tr
><tr id="gr_svn41_278"

><td id="278"><a href="#278">278</a></td></tr
><tr id="gr_svn41_279"

><td id="279"><a href="#279">279</a></td></tr
><tr id="gr_svn41_280"

><td id="280"><a href="#280">280</a></td></tr
><tr id="gr_svn41_281"

><td id="281"><a href="#281">281</a></td></tr
><tr id="gr_svn41_282"

><td id="282"><a href="#282">282</a></td></tr
><tr id="gr_svn41_283"

><td id="283"><a href="#283">283</a></td></tr
><tr id="gr_svn41_284"

><td id="284"><a href="#284">284</a></td></tr
><tr id="gr_svn41_285"

><td id="285"><a href="#285">285</a></td></tr
><tr id="gr_svn41_286"

><td id="286"><a href="#286">286</a></td></tr
><tr id="gr_svn41_287"

><td id="287"><a href="#287">287</a></td></tr
><tr id="gr_svn41_288"

><td id="288"><a href="#288">288</a></td></tr
><tr id="gr_svn41_289"

><td id="289"><a href="#289">289</a></td></tr
><tr id="gr_svn41_290"

><td id="290"><a href="#290">290</a></td></tr
><tr id="gr_svn41_291"

><td id="291"><a href="#291">291</a></td></tr
><tr id="gr_svn41_292"

><td id="292"><a href="#292">292</a></td></tr
><tr id="gr_svn41_293"

><td id="293"><a href="#293">293</a></td></tr
><tr id="gr_svn41_294"

><td id="294"><a href="#294">294</a></td></tr
><tr id="gr_svn41_295"

><td id="295"><a href="#295">295</a></td></tr
><tr id="gr_svn41_296"

><td id="296"><a href="#296">296</a></td></tr
><tr id="gr_svn41_297"

><td id="297"><a href="#297">297</a></td></tr
><tr id="gr_svn41_298"

><td id="298"><a href="#298">298</a></td></tr
><tr id="gr_svn41_299"

><td id="299"><a href="#299">299</a></td></tr
><tr id="gr_svn41_300"

><td id="300"><a href="#300">300</a></td></tr
><tr id="gr_svn41_301"

><td id="301"><a href="#301">301</a></td></tr
><tr id="gr_svn41_302"

><td id="302"><a href="#302">302</a></td></tr
><tr id="gr_svn41_303"

><td id="303"><a href="#303">303</a></td></tr
><tr id="gr_svn41_304"

><td id="304"><a href="#304">304</a></td></tr
><tr id="gr_svn41_305"

><td id="305"><a href="#305">305</a></td></tr
><tr id="gr_svn41_306"

><td id="306"><a href="#306">306</a></td></tr
><tr id="gr_svn41_307"

><td id="307"><a href="#307">307</a></td></tr
><tr id="gr_svn41_308"

><td id="308"><a href="#308">308</a></td></tr
><tr id="gr_svn41_309"

><td id="309"><a href="#309">309</a></td></tr
><tr id="gr_svn41_310"

><td id="310"><a href="#310">310</a></td></tr
><tr id="gr_svn41_311"

><td id="311"><a href="#311">311</a></td></tr
><tr id="gr_svn41_312"

><td id="312"><a href="#312">312</a></td></tr
><tr id="gr_svn41_313"

><td id="313"><a href="#313">313</a></td></tr
><tr id="gr_svn41_314"

><td id="314"><a href="#314">314</a></td></tr
><tr id="gr_svn41_315"

><td id="315"><a href="#315">315</a></td></tr
><tr id="gr_svn41_316"

><td id="316"><a href="#316">316</a></td></tr
><tr id="gr_svn41_317"

><td id="317"><a href="#317">317</a></td></tr
><tr id="gr_svn41_318"

><td id="318"><a href="#318">318</a></td></tr
><tr id="gr_svn41_319"

><td id="319"><a href="#319">319</a></td></tr
><tr id="gr_svn41_320"

><td id="320"><a href="#320">320</a></td></tr
><tr id="gr_svn41_321"

><td id="321"><a href="#321">321</a></td></tr
><tr id="gr_svn41_322"

><td id="322"><a href="#322">322</a></td></tr
><tr id="gr_svn41_323"

><td id="323"><a href="#323">323</a></td></tr
><tr id="gr_svn41_324"

><td id="324"><a href="#324">324</a></td></tr
><tr id="gr_svn41_325"

><td id="325"><a href="#325">325</a></td></tr
><tr id="gr_svn41_326"

><td id="326"><a href="#326">326</a></td></tr
><tr id="gr_svn41_327"

><td id="327"><a href="#327">327</a></td></tr
><tr id="gr_svn41_328"

><td id="328"><a href="#328">328</a></td></tr
><tr id="gr_svn41_329"

><td id="329"><a href="#329">329</a></td></tr
><tr id="gr_svn41_330"

><td id="330"><a href="#330">330</a></td></tr
><tr id="gr_svn41_331"

><td id="331"><a href="#331">331</a></td></tr
><tr id="gr_svn41_332"

><td id="332"><a href="#332">332</a></td></tr
><tr id="gr_svn41_333"

><td id="333"><a href="#333">333</a></td></tr
><tr id="gr_svn41_334"

><td id="334"><a href="#334">334</a></td></tr
><tr id="gr_svn41_335"

><td id="335"><a href="#335">335</a></td></tr
><tr id="gr_svn41_336"

><td id="336"><a href="#336">336</a></td></tr
><tr id="gr_svn41_337"

><td id="337"><a href="#337">337</a></td></tr
><tr id="gr_svn41_338"

><td id="338"><a href="#338">338</a></td></tr
><tr id="gr_svn41_339"

><td id="339"><a href="#339">339</a></td></tr
><tr id="gr_svn41_340"

><td id="340"><a href="#340">340</a></td></tr
><tr id="gr_svn41_341"

><td id="341"><a href="#341">341</a></td></tr
><tr id="gr_svn41_342"

><td id="342"><a href="#342">342</a></td></tr
><tr id="gr_svn41_343"

><td id="343"><a href="#343">343</a></td></tr
><tr id="gr_svn41_344"

><td id="344"><a href="#344">344</a></td></tr
><tr id="gr_svn41_345"

><td id="345"><a href="#345">345</a></td></tr
><tr id="gr_svn41_346"

><td id="346"><a href="#346">346</a></td></tr
><tr id="gr_svn41_347"

><td id="347"><a href="#347">347</a></td></tr
><tr id="gr_svn41_348"

><td id="348"><a href="#348">348</a></td></tr
><tr id="gr_svn41_349"

><td id="349"><a href="#349">349</a></td></tr
><tr id="gr_svn41_350"

><td id="350"><a href="#350">350</a></td></tr
><tr id="gr_svn41_351"

><td id="351"><a href="#351">351</a></td></tr
><tr id="gr_svn41_352"

><td id="352"><a href="#352">352</a></td></tr
><tr id="gr_svn41_353"

><td id="353"><a href="#353">353</a></td></tr
><tr id="gr_svn41_354"

><td id="354"><a href="#354">354</a></td></tr
><tr id="gr_svn41_355"

><td id="355"><a href="#355">355</a></td></tr
><tr id="gr_svn41_356"

><td id="356"><a href="#356">356</a></td></tr
><tr id="gr_svn41_357"

><td id="357"><a href="#357">357</a></td></tr
><tr id="gr_svn41_358"

><td id="358"><a href="#358">358</a></td></tr
><tr id="gr_svn41_359"

><td id="359"><a href="#359">359</a></td></tr
><tr id="gr_svn41_360"

><td id="360"><a href="#360">360</a></td></tr
><tr id="gr_svn41_361"

><td id="361"><a href="#361">361</a></td></tr
><tr id="gr_svn41_362"

><td id="362"><a href="#362">362</a></td></tr
><tr id="gr_svn41_363"

><td id="363"><a href="#363">363</a></td></tr
><tr id="gr_svn41_364"

><td id="364"><a href="#364">364</a></td></tr
><tr id="gr_svn41_365"

><td id="365"><a href="#365">365</a></td></tr
><tr id="gr_svn41_366"

><td id="366"><a href="#366">366</a></td></tr
><tr id="gr_svn41_367"

><td id="367"><a href="#367">367</a></td></tr
><tr id="gr_svn41_368"

><td id="368"><a href="#368">368</a></td></tr
><tr id="gr_svn41_369"

><td id="369"><a href="#369">369</a></td></tr
><tr id="gr_svn41_370"

><td id="370"><a href="#370">370</a></td></tr
><tr id="gr_svn41_371"

><td id="371"><a href="#371">371</a></td></tr
><tr id="gr_svn41_372"

><td id="372"><a href="#372">372</a></td></tr
><tr id="gr_svn41_373"

><td id="373"><a href="#373">373</a></td></tr
><tr id="gr_svn41_374"

><td id="374"><a href="#374">374</a></td></tr
><tr id="gr_svn41_375"

><td id="375"><a href="#375">375</a></td></tr
><tr id="gr_svn41_376"

><td id="376"><a href="#376">376</a></td></tr
><tr id="gr_svn41_377"

><td id="377"><a href="#377">377</a></td></tr
><tr id="gr_svn41_378"

><td id="378"><a href="#378">378</a></td></tr
><tr id="gr_svn41_379"

><td id="379"><a href="#379">379</a></td></tr
><tr id="gr_svn41_380"

><td id="380"><a href="#380">380</a></td></tr
><tr id="gr_svn41_381"

><td id="381"><a href="#381">381</a></td></tr
><tr id="gr_svn41_382"

><td id="382"><a href="#382">382</a></td></tr
><tr id="gr_svn41_383"

><td id="383"><a href="#383">383</a></td></tr
><tr id="gr_svn41_384"

><td id="384"><a href="#384">384</a></td></tr
><tr id="gr_svn41_385"

><td id="385"><a href="#385">385</a></td></tr
><tr id="gr_svn41_386"

><td id="386"><a href="#386">386</a></td></tr
><tr id="gr_svn41_387"

><td id="387"><a href="#387">387</a></td></tr
><tr id="gr_svn41_388"

><td id="388"><a href="#388">388</a></td></tr
><tr id="gr_svn41_389"

><td id="389"><a href="#389">389</a></td></tr
><tr id="gr_svn41_390"

><td id="390"><a href="#390">390</a></td></tr
><tr id="gr_svn41_391"

><td id="391"><a href="#391">391</a></td></tr
><tr id="gr_svn41_392"

><td id="392"><a href="#392">392</a></td></tr
><tr id="gr_svn41_393"

><td id="393"><a href="#393">393</a></td></tr
><tr id="gr_svn41_394"

><td id="394"><a href="#394">394</a></td></tr
><tr id="gr_svn41_395"

><td id="395"><a href="#395">395</a></td></tr
><tr id="gr_svn41_396"

><td id="396"><a href="#396">396</a></td></tr
><tr id="gr_svn41_397"

><td id="397"><a href="#397">397</a></td></tr
><tr id="gr_svn41_398"

><td id="398"><a href="#398">398</a></td></tr
><tr id="gr_svn41_399"

><td id="399"><a href="#399">399</a></td></tr
><tr id="gr_svn41_400"

><td id="400"><a href="#400">400</a></td></tr
><tr id="gr_svn41_401"

><td id="401"><a href="#401">401</a></td></tr
><tr id="gr_svn41_402"

><td id="402"><a href="#402">402</a></td></tr
><tr id="gr_svn41_403"

><td id="403"><a href="#403">403</a></td></tr
><tr id="gr_svn41_404"

><td id="404"><a href="#404">404</a></td></tr
><tr id="gr_svn41_405"

><td id="405"><a href="#405">405</a></td></tr
><tr id="gr_svn41_406"

><td id="406"><a href="#406">406</a></td></tr
><tr id="gr_svn41_407"

><td id="407"><a href="#407">407</a></td></tr
><tr id="gr_svn41_408"

><td id="408"><a href="#408">408</a></td></tr
><tr id="gr_svn41_409"

><td id="409"><a href="#409">409</a></td></tr
><tr id="gr_svn41_410"

><td id="410"><a href="#410">410</a></td></tr
><tr id="gr_svn41_411"

><td id="411"><a href="#411">411</a></td></tr
><tr id="gr_svn41_412"

><td id="412"><a href="#412">412</a></td></tr
><tr id="gr_svn41_413"

><td id="413"><a href="#413">413</a></td></tr
><tr id="gr_svn41_414"

><td id="414"><a href="#414">414</a></td></tr
><tr id="gr_svn41_415"

><td id="415"><a href="#415">415</a></td></tr
><tr id="gr_svn41_416"

><td id="416"><a href="#416">416</a></td></tr
><tr id="gr_svn41_417"

><td id="417"><a href="#417">417</a></td></tr
><tr id="gr_svn41_418"

><td id="418"><a href="#418">418</a></td></tr
><tr id="gr_svn41_419"

><td id="419"><a href="#419">419</a></td></tr
><tr id="gr_svn41_420"

><td id="420"><a href="#420">420</a></td></tr
><tr id="gr_svn41_421"

><td id="421"><a href="#421">421</a></td></tr
><tr id="gr_svn41_422"

><td id="422"><a href="#422">422</a></td></tr
><tr id="gr_svn41_423"

><td id="423"><a href="#423">423</a></td></tr
><tr id="gr_svn41_424"

><td id="424"><a href="#424">424</a></td></tr
><tr id="gr_svn41_425"

><td id="425"><a href="#425">425</a></td></tr
><tr id="gr_svn41_426"

><td id="426"><a href="#426">426</a></td></tr
><tr id="gr_svn41_427"

><td id="427"><a href="#427">427</a></td></tr
><tr id="gr_svn41_428"

><td id="428"><a href="#428">428</a></td></tr
><tr id="gr_svn41_429"

><td id="429"><a href="#429">429</a></td></tr
><tr id="gr_svn41_430"

><td id="430"><a href="#430">430</a></td></tr
><tr id="gr_svn41_431"

><td id="431"><a href="#431">431</a></td></tr
><tr id="gr_svn41_432"

><td id="432"><a href="#432">432</a></td></tr
><tr id="gr_svn41_433"

><td id="433"><a href="#433">433</a></td></tr
><tr id="gr_svn41_434"

><td id="434"><a href="#434">434</a></td></tr
><tr id="gr_svn41_435"

><td id="435"><a href="#435">435</a></td></tr
><tr id="gr_svn41_436"

><td id="436"><a href="#436">436</a></td></tr
><tr id="gr_svn41_437"

><td id="437"><a href="#437">437</a></td></tr
><tr id="gr_svn41_438"

><td id="438"><a href="#438">438</a></td></tr
><tr id="gr_svn41_439"

><td id="439"><a href="#439">439</a></td></tr
><tr id="gr_svn41_440"

><td id="440"><a href="#440">440</a></td></tr
><tr id="gr_svn41_441"

><td id="441"><a href="#441">441</a></td></tr
><tr id="gr_svn41_442"

><td id="442"><a href="#442">442</a></td></tr
><tr id="gr_svn41_443"

><td id="443"><a href="#443">443</a></td></tr
><tr id="gr_svn41_444"

><td id="444"><a href="#444">444</a></td></tr
><tr id="gr_svn41_445"

><td id="445"><a href="#445">445</a></td></tr
><tr id="gr_svn41_446"

><td id="446"><a href="#446">446</a></td></tr
><tr id="gr_svn41_447"

><td id="447"><a href="#447">447</a></td></tr
><tr id="gr_svn41_448"

><td id="448"><a href="#448">448</a></td></tr
><tr id="gr_svn41_449"

><td id="449"><a href="#449">449</a></td></tr
><tr id="gr_svn41_450"

><td id="450"><a href="#450">450</a></td></tr
><tr id="gr_svn41_451"

><td id="451"><a href="#451">451</a></td></tr
><tr id="gr_svn41_452"

><td id="452"><a href="#452">452</a></td></tr
><tr id="gr_svn41_453"

><td id="453"><a href="#453">453</a></td></tr
><tr id="gr_svn41_454"

><td id="454"><a href="#454">454</a></td></tr
><tr id="gr_svn41_455"

><td id="455"><a href="#455">455</a></td></tr
><tr id="gr_svn41_456"

><td id="456"><a href="#456">456</a></td></tr
><tr id="gr_svn41_457"

><td id="457"><a href="#457">457</a></td></tr
><tr id="gr_svn41_458"

><td id="458"><a href="#458">458</a></td></tr
><tr id="gr_svn41_459"

><td id="459"><a href="#459">459</a></td></tr
><tr id="gr_svn41_460"

><td id="460"><a href="#460">460</a></td></tr
><tr id="gr_svn41_461"

><td id="461"><a href="#461">461</a></td></tr
><tr id="gr_svn41_462"

><td id="462"><a href="#462">462</a></td></tr
><tr id="gr_svn41_463"

><td id="463"><a href="#463">463</a></td></tr
><tr id="gr_svn41_464"

><td id="464"><a href="#464">464</a></td></tr
><tr id="gr_svn41_465"

><td id="465"><a href="#465">465</a></td></tr
><tr id="gr_svn41_466"

><td id="466"><a href="#466">466</a></td></tr
><tr id="gr_svn41_467"

><td id="467"><a href="#467">467</a></td></tr
><tr id="gr_svn41_468"

><td id="468"><a href="#468">468</a></td></tr
><tr id="gr_svn41_469"

><td id="469"><a href="#469">469</a></td></tr
><tr id="gr_svn41_470"

><td id="470"><a href="#470">470</a></td></tr
><tr id="gr_svn41_471"

><td id="471"><a href="#471">471</a></td></tr
><tr id="gr_svn41_472"

><td id="472"><a href="#472">472</a></td></tr
><tr id="gr_svn41_473"

><td id="473"><a href="#473">473</a></td></tr
><tr id="gr_svn41_474"

><td id="474"><a href="#474">474</a></td></tr
><tr id="gr_svn41_475"

><td id="475"><a href="#475">475</a></td></tr
><tr id="gr_svn41_476"

><td id="476"><a href="#476">476</a></td></tr
><tr id="gr_svn41_477"

><td id="477"><a href="#477">477</a></td></tr
><tr id="gr_svn41_478"

><td id="478"><a href="#478">478</a></td></tr
><tr id="gr_svn41_479"

><td id="479"><a href="#479">479</a></td></tr
><tr id="gr_svn41_480"

><td id="480"><a href="#480">480</a></td></tr
><tr id="gr_svn41_481"

><td id="481"><a href="#481">481</a></td></tr
><tr id="gr_svn41_482"

><td id="482"><a href="#482">482</a></td></tr
><tr id="gr_svn41_483"

><td id="483"><a href="#483">483</a></td></tr
><tr id="gr_svn41_484"

><td id="484"><a href="#484">484</a></td></tr
><tr id="gr_svn41_485"

><td id="485"><a href="#485">485</a></td></tr
><tr id="gr_svn41_486"

><td id="486"><a href="#486">486</a></td></tr
><tr id="gr_svn41_487"

><td id="487"><a href="#487">487</a></td></tr
><tr id="gr_svn41_488"

><td id="488"><a href="#488">488</a></td></tr
><tr id="gr_svn41_489"

><td id="489"><a href="#489">489</a></td></tr
><tr id="gr_svn41_490"

><td id="490"><a href="#490">490</a></td></tr
><tr id="gr_svn41_491"

><td id="491"><a href="#491">491</a></td></tr
><tr id="gr_svn41_492"

><td id="492"><a href="#492">492</a></td></tr
><tr id="gr_svn41_493"

><td id="493"><a href="#493">493</a></td></tr
><tr id="gr_svn41_494"

><td id="494"><a href="#494">494</a></td></tr
><tr id="gr_svn41_495"

><td id="495"><a href="#495">495</a></td></tr
><tr id="gr_svn41_496"

><td id="496"><a href="#496">496</a></td></tr
><tr id="gr_svn41_497"

><td id="497"><a href="#497">497</a></td></tr
><tr id="gr_svn41_498"

><td id="498"><a href="#498">498</a></td></tr
><tr id="gr_svn41_499"

><td id="499"><a href="#499">499</a></td></tr
><tr id="gr_svn41_500"

><td id="500"><a href="#500">500</a></td></tr
><tr id="gr_svn41_501"

><td id="501"><a href="#501">501</a></td></tr
><tr id="gr_svn41_502"

><td id="502"><a href="#502">502</a></td></tr
><tr id="gr_svn41_503"

><td id="503"><a href="#503">503</a></td></tr
><tr id="gr_svn41_504"

><td id="504"><a href="#504">504</a></td></tr
><tr id="gr_svn41_505"

><td id="505"><a href="#505">505</a></td></tr
><tr id="gr_svn41_506"

><td id="506"><a href="#506">506</a></td></tr
><tr id="gr_svn41_507"

><td id="507"><a href="#507">507</a></td></tr
><tr id="gr_svn41_508"

><td id="508"><a href="#508">508</a></td></tr
><tr id="gr_svn41_509"

><td id="509"><a href="#509">509</a></td></tr
><tr id="gr_svn41_510"

><td id="510"><a href="#510">510</a></td></tr
><tr id="gr_svn41_511"

><td id="511"><a href="#511">511</a></td></tr
><tr id="gr_svn41_512"

><td id="512"><a href="#512">512</a></td></tr
><tr id="gr_svn41_513"

><td id="513"><a href="#513">513</a></td></tr
><tr id="gr_svn41_514"

><td id="514"><a href="#514">514</a></td></tr
><tr id="gr_svn41_515"

><td id="515"><a href="#515">515</a></td></tr
><tr id="gr_svn41_516"

><td id="516"><a href="#516">516</a></td></tr
><tr id="gr_svn41_517"

><td id="517"><a href="#517">517</a></td></tr
><tr id="gr_svn41_518"

><td id="518"><a href="#518">518</a></td></tr
><tr id="gr_svn41_519"

><td id="519"><a href="#519">519</a></td></tr
><tr id="gr_svn41_520"

><td id="520"><a href="#520">520</a></td></tr
><tr id="gr_svn41_521"

><td id="521"><a href="#521">521</a></td></tr
><tr id="gr_svn41_522"

><td id="522"><a href="#522">522</a></td></tr
><tr id="gr_svn41_523"

><td id="523"><a href="#523">523</a></td></tr
><tr id="gr_svn41_524"

><td id="524"><a href="#524">524</a></td></tr
><tr id="gr_svn41_525"

><td id="525"><a href="#525">525</a></td></tr
><tr id="gr_svn41_526"

><td id="526"><a href="#526">526</a></td></tr
><tr id="gr_svn41_527"

><td id="527"><a href="#527">527</a></td></tr
><tr id="gr_svn41_528"

><td id="528"><a href="#528">528</a></td></tr
><tr id="gr_svn41_529"

><td id="529"><a href="#529">529</a></td></tr
><tr id="gr_svn41_530"

><td id="530"><a href="#530">530</a></td></tr
><tr id="gr_svn41_531"

><td id="531"><a href="#531">531</a></td></tr
><tr id="gr_svn41_532"

><td id="532"><a href="#532">532</a></td></tr
><tr id="gr_svn41_533"

><td id="533"><a href="#533">533</a></td></tr
><tr id="gr_svn41_534"

><td id="534"><a href="#534">534</a></td></tr
><tr id="gr_svn41_535"

><td id="535"><a href="#535">535</a></td></tr
><tr id="gr_svn41_536"

><td id="536"><a href="#536">536</a></td></tr
><tr id="gr_svn41_537"

><td id="537"><a href="#537">537</a></td></tr
><tr id="gr_svn41_538"

><td id="538"><a href="#538">538</a></td></tr
><tr id="gr_svn41_539"

><td id="539"><a href="#539">539</a></td></tr
><tr id="gr_svn41_540"

><td id="540"><a href="#540">540</a></td></tr
><tr id="gr_svn41_541"

><td id="541"><a href="#541">541</a></td></tr
><tr id="gr_svn41_542"

><td id="542"><a href="#542">542</a></td></tr
><tr id="gr_svn41_543"

><td id="543"><a href="#543">543</a></td></tr
><tr id="gr_svn41_544"

><td id="544"><a href="#544">544</a></td></tr
><tr id="gr_svn41_545"

><td id="545"><a href="#545">545</a></td></tr
><tr id="gr_svn41_546"

><td id="546"><a href="#546">546</a></td></tr
><tr id="gr_svn41_547"

><td id="547"><a href="#547">547</a></td></tr
><tr id="gr_svn41_548"

><td id="548"><a href="#548">548</a></td></tr
><tr id="gr_svn41_549"

><td id="549"><a href="#549">549</a></td></tr
><tr id="gr_svn41_550"

><td id="550"><a href="#550">550</a></td></tr
><tr id="gr_svn41_551"

><td id="551"><a href="#551">551</a></td></tr
><tr id="gr_svn41_552"

><td id="552"><a href="#552">552</a></td></tr
><tr id="gr_svn41_553"

><td id="553"><a href="#553">553</a></td></tr
></table></pre>
<pre><table width="100%"><tr class="nocursor"><td></td></tr></table></pre>
</td>
<td id="lines">
<pre><table width="100%"><tr class="cursor_stop cursor_hidden"><td></td></tr></table></pre>
<pre class="prettyprint lang-py"><table id="src_table_0"><tr
id=sl_svn41_1

><td class="source">import os, socket, threading,\<br></td></tr
><tr
id=sl_svn41_2

><td class="source">       logging, sys, signal<br></td></tr
><tr
id=sl_svn41_3

><td class="source">import subprocess, time<br></td></tr
><tr
id=sl_svn41_4

><td class="source">import shutil,random,math<br></td></tr
><tr
id=sl_svn41_5

><td class="source">import Pyro.core, Pyro.naming<br></td></tr
><tr
id=sl_svn41_6

><td class="source">from remoteClass import remoteClass<br></td></tr
><tr
id=sl_svn41_7

><td class="source">from ControlClass import ControlClass<br></td></tr
><tr
id=sl_svn41_8

><td class="source">from hashlib import sha1<br></td></tr
><tr
id=sl_svn41_9

><td class="source">from ChordProcessRecord import ChordProcessRecord<br></td></tr
><tr
id=sl_svn41_10

><td class="source">from fileObject import fileObject<br></td></tr
><tr
id=sl_svn41_11

><td class="source">import thread<br></td></tr
><tr
id=sl_svn41_12

><td class="source">#Enable debugging/ send to stderr<br></td></tr
><tr
id=sl_svn41_13

><td class="source">#logging.basicConfig(level=logging.DEBUG)<br></td></tr
><tr
id=sl_svn41_14

><td class="source"><br></td></tr
><tr
id=sl_svn41_15

><td class="source">class ChordProcess(threading.Thread):<br></td></tr
><tr
id=sl_svn41_16

><td class="source">    <br></td></tr
><tr
id=sl_svn41_17

><td class="source">    SUCCESSOR_LIST_SIZE = 6 <br></td></tr
><tr
id=sl_svn41_18

><td class="source">    KEY_LENGTH = 32<br></td></tr
><tr
id=sl_svn41_19

><td class="source">    LOOKUP_RETRIES = 5<br></td></tr
><tr
id=sl_svn41_20

><td class="source">    PERIOD = 3<br></td></tr
><tr
id=sl_svn41_21

><td class="source">    CHURN_RATE = 0<br></td></tr
><tr
id=sl_svn41_22

><td class="source">    MIN_EXP_TIME = 8<br></td></tr
><tr
id=sl_svn41_23

><td class="source">    <br></td></tr
><tr
id=sl_svn41_24

><td class="source">    def __init__(self,portNumber,bootstrapNodePort,churn,controlPortNumber):<br></td></tr
><tr
id=sl_svn41_25

><td class="source">        &quot;Chord Process constructor&quot;<br></td></tr
><tr
id=sl_svn41_26

><td class="source">        threading.Thread.__init__(self)<br></td></tr
><tr
id=sl_svn41_27

><td class="source">        <br></td></tr
><tr
id=sl_svn41_28

><td class="source">        <br></td></tr
><tr
id=sl_svn41_29

><td class="source">        # CHORD Client constructs<br></td></tr
><tr
id=sl_svn41_30

><td class="source">        self._successor     = ChordProcessRecord()<br></td></tr
><tr
id=sl_svn41_31

><td class="source">        self._predecessor   = ChordProcessRecord()<br></td></tr
><tr
id=sl_svn41_32

><td class="source">        self._successorList = range(1,self.SUCCESSOR_LIST_SIZE)<br></td></tr
><tr
id=sl_svn41_33

><td class="source">        <br></td></tr
><tr
id=sl_svn41_34

><td class="source">        # &quot;Initialize&quot; the finger Table<br></td></tr
><tr
id=sl_svn41_35

><td class="source">        self._fingerTable = range(0,self.KEY_LENGTH)<br></td></tr
><tr
id=sl_svn41_36

><td class="source">        <br></td></tr
><tr
id=sl_svn41_37

><td class="source">        # Use the process id as unique id<br></td></tr
><tr
id=sl_svn41_38

><td class="source">        self._processID  = os.getpid()<br></td></tr
><tr
id=sl_svn41_39

><td class="source">        self._localClient = ChordProcessRecord(self.assignHashKey(portNumber),int(portNumber))<br></td></tr
><tr
id=sl_svn41_40

><td class="source">        self._bootstrapNodePort = int(bootstrapNodePort)<br></td></tr
><tr
id=sl_svn41_41

><td class="source">        self._remoteClassInstance = remoteClass(self)<br></td></tr
><tr
id=sl_svn41_42

><td class="source">        self._controlClassInstance = ControlClass(self)<br></td></tr
><tr
id=sl_svn41_43

><td class="source">        self.CHURN_RATE = churn<br></td></tr
><tr
id=sl_svn41_44

><td class="source">        # Initialize the next pointer for use in fingerTable<br></td></tr
><tr
id=sl_svn41_45

><td class="source">        self._next = 0<br></td></tr
><tr
id=sl_svn41_46

><td class="source">        self._fingerTableFull =False<br></td></tr
><tr
id=sl_svn41_47

><td class="source">        # Process is &quot;ON&quot;<br></td></tr
><tr
id=sl_svn41_48

><td class="source">        self._status = True<br></td></tr
><tr
id=sl_svn41_49

><td class="source">        <br></td></tr
><tr
id=sl_svn41_50

><td class="source">        # Create directory for file storing<br></td></tr
><tr
id=sl_svn41_51

><td class="source">        self._dir = self.createDir()<br></td></tr
><tr
id=sl_svn41_52

><td class="source">        # Start local server<br></td></tr
><tr
id=sl_svn41_53

><td class="source">        thread.start_new_thread(self.localServer,())<br></td></tr
><tr
id=sl_svn41_54

><td class="source">        <br></td></tr
><tr
id=sl_svn41_55

><td class="source">        # Find the server of the Chord Control process<br></td></tr
><tr
id=sl_svn41_56

><td class="source">        self._controlProcess = Pyro.core.getProxyForURI(&quot;PYRONAME://{0}&quot;.format(controlPortNumber)) <br></td></tr
><tr
id=sl_svn41_57

><td class="source">        <br></td></tr
><tr
id=sl_svn41_58

><td class="source">        print &quot;Node {0} activated on port {1}.&quot;.format(self._localClient.getKey(),self._localClient.getPortNumber())    <br></td></tr
><tr
id=sl_svn41_59

><td class="source">    <br></td></tr
><tr
id=sl_svn41_60

><td class="source">    def assignHashKey(self,objectID):<br></td></tr
><tr
id=sl_svn41_61

><td class="source">        &quot;Given an objectID,returns a unique\<br></td></tr
><tr
id=sl_svn41_62

><td class="source">        160-bit key, using SHA1.&quot; <br></td></tr
><tr
id=sl_svn41_63

><td class="source">        #Call the SHA-1 function to get a key<br></td></tr
><tr
id=sl_svn41_64

><td class="source">        <br></td></tr
><tr
id=sl_svn41_65

><td class="source">        key = sha1(repr(objectID)).hexdigest()<br></td></tr
><tr
id=sl_svn41_66

><td class="source">        return key[(160-self.KEY_LENGTH)/4:]<br></td></tr
><tr
id=sl_svn41_67

><td class="source"><br></td></tr
><tr
id=sl_svn41_68

><td class="source">    def createDir(self):<br></td></tr
><tr
id=sl_svn41_69

><td class="source">        &quot;Make a new folder on the disk for storing files. If there already is one do nothing&quot;<br></td></tr
><tr
id=sl_svn41_70

><td class="source">        if not os.path.isdir(self._localClient.getKey()):<br></td></tr
><tr
id=sl_svn41_71

><td class="source">            #logging.debug(&quot;Creating folder {0}....&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_72

><td class="source">            os.mkdir(self._localClient.getKey())<br></td></tr
><tr
id=sl_svn41_73

><td class="source">        return self._localClient.getKey()<br></td></tr
><tr
id=sl_svn41_74

><td class="source">    <br></td></tr
><tr
id=sl_svn41_75

><td class="source">    def getfileExists(self,fileName):<br></td></tr
><tr
id=sl_svn41_76

><td class="source">        &quot;Given a fileName it returns True if the file exists \<br></td></tr
><tr
id=sl_svn41_77

><td class="source">        on the disc or False otherwise&quot;<br></td></tr
><tr
id=sl_svn41_78

><td class="source">        if os.path.isfile(self._dir + &#39;/&#39; + fileName):<br></td></tr
><tr
id=sl_svn41_79

><td class="source">            return True<br></td></tr
><tr
id=sl_svn41_80

><td class="source">        else:<br></td></tr
><tr
id=sl_svn41_81

><td class="source">            return False<br></td></tr
><tr
id=sl_svn41_82

><td class="source">    <br></td></tr
><tr
id=sl_svn41_83

><td class="source">    def localServer(self):<br></td></tr
><tr
id=sl_svn41_84

><td class="source">        &quot;A second thread of execution, upon which\<br></td></tr
><tr
id=sl_svn41_85

><td class="source">        a server is running, in order to read any\<br></td></tr
><tr
id=sl_svn41_86

><td class="source">        incoming requests&quot;<br></td></tr
><tr
id=sl_svn41_87

><td class="source">        <br></td></tr
><tr
id=sl_svn41_88

><td class="source">        Pyro.core.initServer()<br></td></tr
><tr
id=sl_svn41_89

><td class="source">        ns=Pyro.naming.NameServerLocator().getNS()<br></td></tr
><tr
id=sl_svn41_90

><td class="source">        self._daemon=Pyro.core.Daemon()<br></td></tr
><tr
id=sl_svn41_91

><td class="source">        self._daemon.useNameServer(ns)<br></td></tr
><tr
id=sl_svn41_92

><td class="source">        <br></td></tr
><tr
id=sl_svn41_93

><td class="source">        uri=self._daemon.connect(self._remoteClassInstance,str(self._localClient.getPortNumber()))<br></td></tr
><tr
id=sl_svn41_94

><td class="source">        <br></td></tr
><tr
id=sl_svn41_95

><td class="source">        logging.debug(&quot;{0}: Listening for incoming messages on {1}:{2}&quot;.format(self._localClient.getKey(),uri,self._daemon.port))<br></td></tr
><tr
id=sl_svn41_96

><td class="source">        <br></td></tr
><tr
id=sl_svn41_97

><td class="source">        self._daemon.setTimeout(3) <br></td></tr
><tr
id=sl_svn41_98

><td class="source">        self._daemon.requestLoop()<br></td></tr
><tr
id=sl_svn41_99

><td class="source">        <br></td></tr
><tr
id=sl_svn41_100

><td class="source">        thread.exit()<br></td></tr
><tr
id=sl_svn41_101

><td class="source">        <br></td></tr
><tr
id=sl_svn41_102

><td class="source">    def controlServer(self):<br></td></tr
><tr
id=sl_svn41_103

><td class="source">        <br></td></tr
><tr
id=sl_svn41_104

><td class="source">        Pyro.core.initServer()<br></td></tr
><tr
id=sl_svn41_105

><td class="source">        ns=Pyro.naming.NameServerLocator().getNS()<br></td></tr
><tr
id=sl_svn41_106

><td class="source">        self._cdaemon=Pyro.core.Daemon()<br></td></tr
><tr
id=sl_svn41_107

><td class="source">        self._cdaemon.useNameServer(ns)<br></td></tr
><tr
id=sl_svn41_108

><td class="source">        <br></td></tr
><tr
id=sl_svn41_109

><td class="source">        uri=self._cdaemon.connect(self._controlClassInstance,str(self._localClient.getPortNumber()+1))<br></td></tr
><tr
id=sl_svn41_110

><td class="source">        <br></td></tr
><tr
id=sl_svn41_111

><td class="source">        logging.debug(&quot;{0}: Listening for Control messages on {1}:{2}&quot;.format(self._localClient.getKey(),uri,self._cdaemon.port))<br></td></tr
><tr
id=sl_svn41_112

><td class="source">        <br></td></tr
><tr
id=sl_svn41_113

><td class="source">        self._cdaemon.requestLoop() <br></td></tr
><tr
id=sl_svn41_114

><td class="source">    <br></td></tr
><tr
id=sl_svn41_115

><td class="source">    def localFileInsert(self,fileName):<br></td></tr
><tr
id=sl_svn41_116

><td class="source">        &quot;Copies the given file to the self._dir directory&quot;<br></td></tr
><tr
id=sl_svn41_117

><td class="source">        try:<br></td></tr
><tr
id=sl_svn41_118

><td class="source">            shutil.move(fileName,self._dir + &#39;/&#39; + fileName)<br></td></tr
><tr
id=sl_svn41_119

><td class="source">            #logging.debug(&quot;File copied locally succesfully&quot;)<br></td></tr
><tr
id=sl_svn41_120

><td class="source">            return True<br></td></tr
><tr
id=sl_svn41_121

><td class="source">        except:<br></td></tr
><tr
id=sl_svn41_122

><td class="source">            #logging.error(&quot;Local File copy failed&quot;)<br></td></tr
><tr
id=sl_svn41_123

><td class="source">            return False<br></td></tr
><tr
id=sl_svn41_124

><td class="source">            <br></td></tr
><tr
id=sl_svn41_125

><td class="source">    <br></td></tr
><tr
id=sl_svn41_126

><td class="source">    def fileInsert(self,fileName):<br></td></tr
><tr
id=sl_svn41_127

><td class="source">        &quot;Given the name of a file, this method inserts the\<br></td></tr
><tr
id=sl_svn41_128

><td class="source">         file into the CHORD DHT&quot;<br></td></tr
><tr
id=sl_svn41_129

><td class="source">         <br></td></tr
><tr
id=sl_svn41_130

><td class="source">        file = fileObject(fileName,self.assignHashKey(fileName)) <br></td></tr
><tr
id=sl_svn41_131

><td class="source">        fileSuccessor = self.lookup(file.getKey())<br></td></tr
><tr
id=sl_svn41_132

><td class="source">        print &quot;Key of file {0} is {1}&quot;.format(fileName,file.getKey())<br></td></tr
><tr
id=sl_svn41_133

><td class="source">        if fileSuccessor.getKey() == self._localClient.getKey():<br></td></tr
><tr
id=sl_svn41_134

><td class="source">            self.localFileInsert(fileName)<br></td></tr
><tr
id=sl_svn41_135

><td class="source">            logging.debug(&quot;File {0} successfully inserted locally&quot;.format(file.getName()))<br></td></tr
><tr
id=sl_svn41_136

><td class="source">        else:<br></td></tr
><tr
id=sl_svn41_137

><td class="source">            logging.debug(&quot;Inserting file: {0} to node {1}&quot;.format(file.getName(),fileSuccessor.getKey()))<br></td></tr
><tr
id=sl_svn41_138

><td class="source">            if fileSuccessor.passFile(file):<br></td></tr
><tr
id=sl_svn41_139

><td class="source">                #logging.debug(&quot;File copied successfully&quot;)<br></td></tr
><tr
id=sl_svn41_140

><td class="source">                return True<br></td></tr
><tr
id=sl_svn41_141

><td class="source">            else:<br></td></tr
><tr
id=sl_svn41_142

><td class="source">                #logging.error(&quot;File copy failed&quot;)<br></td></tr
><tr
id=sl_svn41_143

><td class="source">                return False<br></td></tr
><tr
id=sl_svn41_144

><td class="source">              <br></td></tr
><tr
id=sl_svn41_145

><td class="source">    def getPassedFile(self,file):<br></td></tr
><tr
id=sl_svn41_146

><td class="source">        &quot;Stores the file on the local directory&quot;<br></td></tr
><tr
id=sl_svn41_147

><td class="source">        try:<br></td></tr
><tr
id=sl_svn41_148

><td class="source">            self.makeFileObjectIntoFile(file)<br></td></tr
><tr
id=sl_svn41_149

><td class="source">            return True<br></td></tr
><tr
id=sl_svn41_150

><td class="source">        except:<br></td></tr
><tr
id=sl_svn41_151

><td class="source">            return False<br></td></tr
><tr
id=sl_svn41_152

><td class="source">    <br></td></tr
><tr
id=sl_svn41_153

><td class="source">    def makeFileObjectIntoFile(self,file):<br></td></tr
><tr
id=sl_svn41_154

><td class="source">        &quot;Creates a file from a list which contains lines of files&quot;<br></td></tr
><tr
id=sl_svn41_155

><td class="source">        f = open(self._dir + &#39;/&#39; + file.getName(),&#39;a&#39;)<br></td></tr
><tr
id=sl_svn41_156

><td class="source">        for line in file.getData():<br></td></tr
><tr
id=sl_svn41_157

><td class="source">            f.write(line)<br></td></tr
><tr
id=sl_svn41_158

><td class="source">        f.close()<br></td></tr
><tr
id=sl_svn41_159

><td class="source">            <br></td></tr
><tr
id=sl_svn41_160

><td class="source">        <br></td></tr
><tr
id=sl_svn41_161

><td class="source">    def fileSearch(self,fileName):<br></td></tr
><tr
id=sl_svn41_162

><td class="source">        &quot;Given a file name, this process makes a\<br></td></tr
><tr
id=sl_svn41_163

><td class="source">        lookup for the file over the CHORD DHT&quot;<br></td></tr
><tr
id=sl_svn41_164

><td class="source"><br></td></tr
><tr
id=sl_svn41_165

><td class="source">        fileKey = self.assignHashKey(fileName)<br></td></tr
><tr
id=sl_svn41_166

><td class="source">        (fileSuccessor,steps) = self.lookup(fileKey,0)<br></td></tr
><tr
id=sl_svn41_167

><td class="source">        if fileSuccessor.fileExists(fileName):<br></td></tr
><tr
id=sl_svn41_168

><td class="source">            logging.debug(&quot;{0}: File {1} exists in {2}&quot;.format(self._localClient.getKey(),fileName,fileSuccessor.getKey()))<br></td></tr
><tr
id=sl_svn41_169

><td class="source">            return fileSuccessor.getKey(),steps<br></td></tr
><tr
id=sl_svn41_170

><td class="source">        else:<br></td></tr
><tr
id=sl_svn41_171

><td class="source">            logging.warning(&quot;{0}: File {1} could not be found&quot;.format(self._localClient.getKey(),fileName))<br></td></tr
><tr
id=sl_svn41_172

><td class="source">            return None,steps<br></td></tr
><tr
id=sl_svn41_173

><td class="source">        <br></td></tr
><tr
id=sl_svn41_174

><td class="source">        <br></td></tr
><tr
id=sl_svn41_175

><td class="source">    def lookup(self,lookupKey,steps = None):<br></td></tr
><tr
id=sl_svn41_176

><td class="source">        &quot;Given a lookup key, this method returns the\<br></td></tr
><tr
id=sl_svn41_177

><td class="source">        IP address(port Number) of the process that is the\<br></td></tr
><tr
id=sl_svn41_178

><td class="source">         successor(lookupKey)&quot;<br></td></tr
><tr
id=sl_svn41_179

><td class="source">        <br></td></tr
><tr
id=sl_svn41_180

><td class="source">        #logging.debug(&quot;Lookup:{0}: Looking up key {1}&quot;.format(self._localClient.getKey(),lookupKey))<br></td></tr
><tr
id=sl_svn41_181

><td class="source">        if self.isInRange(self._localClient.getKey(),self._successor.getKey(),lookupKey,&quot;&gt;=&quot;):<br></td></tr
><tr
id=sl_svn41_182

><td class="source">            if steps != None:<br></td></tr
><tr
id=sl_svn41_183

><td class="source">                return (self._successor,steps+1)<br></td></tr
><tr
id=sl_svn41_184

><td class="source">            else:<br></td></tr
><tr
id=sl_svn41_185

><td class="source">                return self._successor<br></td></tr
><tr
id=sl_svn41_186

><td class="source">        else :<br></td></tr
><tr
id=sl_svn41_187

><td class="source">            #logging.debug(&quot;Lookup: looking into the finger table for key:{0}&quot;.format(lookupKey))<br></td></tr
><tr
id=sl_svn41_188

><td class="source">            if steps!=None:<br></td></tr
><tr
id=sl_svn41_189

><td class="source">                precedingNode,retSteps = self.findSuccessor(self.closestPrecedingNode(lookupKey),lookupKey,steps)<br></td></tr
><tr
id=sl_svn41_190

><td class="source">            else:<br></td></tr
><tr
id=sl_svn41_191

><td class="source">                precedingNode = self.findSuccessor(self.closestPrecedingNode(lookupKey),lookupKey)<br></td></tr
><tr
id=sl_svn41_192

><td class="source">            if not precedingNode.isSet():<br></td></tr
><tr
id=sl_svn41_193

><td class="source">                logging.debug(&quot;{0} Lookup: Preceding node is not set.&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_194

><td class="source">            if steps != None:<br></td></tr
><tr
id=sl_svn41_195

><td class="source">                return (precedingNode,retSteps+1)<br></td></tr
><tr
id=sl_svn41_196

><td class="source">            else:<br></td></tr
><tr
id=sl_svn41_197

><td class="source">                return precedingNode<br></td></tr
><tr
id=sl_svn41_198

><td class="source">    <br></td></tr
><tr
id=sl_svn41_199

><td class="source">    def findSuccessor(self,node,lookupKey,steps = None):<br></td></tr
><tr
id=sl_svn41_200

><td class="source">        i=0<br></td></tr
><tr
id=sl_svn41_201

><td class="source">        success = False<br></td></tr
><tr
id=sl_svn41_202

><td class="source">        while success == False and i &lt; self.LOOKUP_RETRIES :<br></td></tr
><tr
id=sl_svn41_203

><td class="source">            i = i+1<br></td></tr
><tr
id=sl_svn41_204

><td class="source">            try:<br></td></tr
><tr
id=sl_svn41_205

><td class="source">                node = node.findSuccessor(lookupKey,steps)<br></td></tr
><tr
id=sl_svn41_206

><td class="source">                success = True<br></td></tr
><tr
id=sl_svn41_207

><td class="source">            except:<br></td></tr
><tr
id=sl_svn41_208

><td class="source">                # find the next best preceding node of the lookupKey<br></td></tr
><tr
id=sl_svn41_209

><td class="source">                node = self.closestPrecedingNode(node.getKey())<br></td></tr
><tr
id=sl_svn41_210

><td class="source">                logging.debug(&quot;{0} Find successor failed.Trying node {1}&quot;.format(self._localClient.getKey(),node.getKey()))<br></td></tr
><tr
id=sl_svn41_211

><td class="source">        <br></td></tr
><tr
id=sl_svn41_212

><td class="source">        return node<br></td></tr
><tr
id=sl_svn41_213

><td class="source">            <br></td></tr
><tr
id=sl_svn41_214

><td class="source"><br></td></tr
><tr
id=sl_svn41_215

><td class="source">    def isInRange(self,startKey,endKey,searchKey,comparator = &quot;&gt;&quot;):<br></td></tr
><tr
id=sl_svn41_216

><td class="source">        &quot;Returns True if the searchKey is between the\<br></td></tr
><tr
id=sl_svn41_217

><td class="source">        startKey and the endKey in the CHORD ring&quot;<br></td></tr
><tr
id=sl_svn41_218

><td class="source">        if comparator == &quot;&gt;&quot;:<br></td></tr
><tr
id=sl_svn41_219

><td class="source">            comparison= startKey &gt; endKey<br></td></tr
><tr
id=sl_svn41_220

><td class="source">        else :<br></td></tr
><tr
id=sl_svn41_221

><td class="source">            comparison= startKey &gt;= endKey<br></td></tr
><tr
id=sl_svn41_222

><td class="source">        <br></td></tr
><tr
id=sl_svn41_223

><td class="source">        if comparison:<br></td></tr
><tr
id=sl_svn41_224

><td class="source">            if searchKey &gt; startKey or searchKey &lt; endKey:<br></td></tr
><tr
id=sl_svn41_225

><td class="source">                return True<br></td></tr
><tr
id=sl_svn41_226

><td class="source">        elif searchKey &gt; startKey and searchKey &lt; endKey:<br></td></tr
><tr
id=sl_svn41_227

><td class="source">            return True<br></td></tr
><tr
id=sl_svn41_228

><td class="source">        return False<br></td></tr
><tr
id=sl_svn41_229

><td class="source">            <br></td></tr
><tr
id=sl_svn41_230

><td class="source">    def closestPrecedingNode(self,lookupKey):<br></td></tr
><tr
id=sl_svn41_231

><td class="source">        &quot;Given a lookupKey, the successor list and finger table\<br></td></tr
><tr
id=sl_svn41_232

><td class="source">        is accessed in order to find the node that is preceding the\<br></td></tr
><tr
id=sl_svn41_233

><td class="source">        lookup key, and is the closest to it.&quot;<br></td></tr
><tr
id=sl_svn41_234

><td class="source">        closestNode = ChordProcessRecord()<br></td></tr
><tr
id=sl_svn41_235

><td class="source">        #First find the closest preceding node in the successor list<br></td></tr
><tr
id=sl_svn41_236

><td class="source">        for pos in range(len(self._successorList)-1,-1,-1): <br></td></tr
><tr
id=sl_svn41_237

><td class="source">            node = self._successorList[pos]<br></td></tr
><tr
id=sl_svn41_238

><td class="source">            if self.isInRange(self._localClient.getKey(), lookupKey, node.getKey()): <br></td></tr
><tr
id=sl_svn41_239

><td class="source">                closestNode = node;<br></td></tr
><tr
id=sl_svn41_240

><td class="source">                break<br></td></tr
><tr
id=sl_svn41_241

><td class="source">            <br></td></tr
><tr
id=sl_svn41_242

><td class="source">        if self._fingerTableFull:<br></td></tr
><tr
id=sl_svn41_243

><td class="source">            length = self.KEY_LENGTH-1<br></td></tr
><tr
id=sl_svn41_244

><td class="source">        else :<br></td></tr
><tr
id=sl_svn41_245

><td class="source">            length = self._next-1<br></td></tr
><tr
id=sl_svn41_246

><td class="source">            <br></td></tr
><tr
id=sl_svn41_247

><td class="source">        <br></td></tr
><tr
id=sl_svn41_248

><td class="source">        #Then find the closest preceding node in the finger table<br></td></tr
><tr
id=sl_svn41_249

><td class="source">        for pos in range(length,-1,-1):<br></td></tr
><tr
id=sl_svn41_250

><td class="source">            currentKey = self._fingerTable[pos].getKey() <br></td></tr
><tr
id=sl_svn41_251

><td class="source">            if self.isInRange(self._localClient.getKey(),lookupKey,currentKey):<br></td></tr
><tr
id=sl_svn41_252

><td class="source">                if closestNode.isSet():<br></td></tr
><tr
id=sl_svn41_253

><td class="source">                    # If the closest node found in the successor list is closer to the key...<br></td></tr
><tr
id=sl_svn41_254

><td class="source">                    if not self.isInRange(self._localClient.getKey(),currentKey,closestNode.getKey()):<br></td></tr
><tr
id=sl_svn41_255

><td class="source">                        # ...then return the closest node in the successor list<br></td></tr
><tr
id=sl_svn41_256

><td class="source">                        return closestNode<br></td></tr
><tr
id=sl_svn41_257

><td class="source">                else:<br></td></tr
><tr
id=sl_svn41_258

><td class="source">                        #... else return the finger table entry<br></td></tr
><tr
id=sl_svn41_259

><td class="source">                        return self._fingerTable[pos]<br></td></tr
><tr
id=sl_svn41_260

><td class="source">                    <br></td></tr
><tr
id=sl_svn41_261

><td class="source">        if closestNode.isSet():<br></td></tr
><tr
id=sl_svn41_262

><td class="source">            return closestNode<br></td></tr
><tr
id=sl_svn41_263

><td class="source">                <br></td></tr
><tr
id=sl_svn41_264

><td class="source">        return self._localClient<br></td></tr
><tr
id=sl_svn41_265

><td class="source">        <br></td></tr
><tr
id=sl_svn41_266

><td class="source">    def getProxy(self,portNumber):<br></td></tr
><tr
id=sl_svn41_267

><td class="source">        &quot;Given the port in the name service,\<br></td></tr
><tr
id=sl_svn41_268

><td class="source">        returns a proxy of the remote object&quot;<br></td></tr
><tr
id=sl_svn41_269

><td class="source">        return  Pyro.core.getProxyForURI(&quot;PYRONAME://{0}&quot;.format(portNumber))<br></td></tr
><tr
id=sl_svn41_270

><td class="source">        <br></td></tr
><tr
id=sl_svn41_271

><td class="source">    def nodeJoin(self):<br></td></tr
><tr
id=sl_svn41_272

><td class="source">        &quot;Given a node to contact (class var), this method\<br></td></tr
><tr
id=sl_svn41_273

><td class="source">        puts the current Client in the Chord DHT. Returns TRUE\<br></td></tr
><tr
id=sl_svn41_274

><td class="source">        if the operation is successful, otherwise FALSE.\<br></td></tr
><tr
id=sl_svn41_275

><td class="source">        If contactNode is NONE, then a new ring is created.&quot;<br></td></tr
><tr
id=sl_svn41_276

><td class="source">        logging.debug(&quot;{0}:Attempting to join the CHORD network&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_277

><td class="source">        if self._bootstrapNodePort == self._localClient.getPortNumber():<br></td></tr
><tr
id=sl_svn41_278

><td class="source">            logging.debug(&quot;{0}:Creating a new Ring&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_279

><td class="source">            return self.createRing()<br></td></tr
><tr
id=sl_svn41_280

><td class="source">        else:<br></td></tr
><tr
id=sl_svn41_281

><td class="source">            self._predecessor = ChordProcessRecord()<br></td></tr
><tr
id=sl_svn41_282

><td class="source">            proxy = self.getProxy(self._bootstrapNodePort)<br></td></tr
><tr
id=sl_svn41_283

><td class="source">            self._successor   = proxy.findSuccessor(self._localClient.getKey())<br></td></tr
><tr
id=sl_svn41_284

><td class="source">            self._successorList = [self._successor for item in  range(0,self.SUCCESSOR_LIST_SIZE)]<br></td></tr
><tr
id=sl_svn41_285

><td class="source">            logging.debug(&quot;{0}:Successor found:{1}&quot;.format(self._localClient.getKey(),self._successor.getKey()))<br></td></tr
><tr
id=sl_svn41_286

><td class="source">            if self._successor.getKey() != self._localClient.getKey():<br></td></tr
><tr
id=sl_svn41_287

><td class="source">                fileObjectList = self._successor.getFiles()<br></td></tr
><tr
id=sl_svn41_288

><td class="source">                self.writeFileObjectsToDisk(fileObjectList)<br></td></tr
><tr
id=sl_svn41_289

><td class="source">            return True    <br></td></tr
><tr
id=sl_svn41_290

><td class="source">    <br></td></tr
><tr
id=sl_svn41_291

><td class="source">    def  writeFileObjectsToDisk(self,fileObjectList):<br></td></tr
><tr
id=sl_svn41_292

><td class="source">        &quot;Given a list of fileObjects, this function creates files\<br></td></tr
><tr
id=sl_svn41_293

><td class="source">        for each one of them&quot;<br></td></tr
><tr
id=sl_svn41_294

><td class="source">        #logging.debug(&quot;Retrieved {0} files from successor&quot;.format(len(fileObjectList)))<br></td></tr
><tr
id=sl_svn41_295

><td class="source">        for item in fileObjectList:<br></td></tr
><tr
id=sl_svn41_296

><td class="source">            self.makeFileObjectIntoFile(item)<br></td></tr
><tr
id=sl_svn41_297

><td class="source">            <br></td></tr
><tr
id=sl_svn41_298

><td class="source">    def getFiles(self):<br></td></tr
><tr
id=sl_svn41_299

><td class="source">        &quot;Called upon join of a predecessor.Returns a\<br></td></tr
><tr
id=sl_svn41_300

><td class="source">        fileObject list of the files that should be moved\<br></td></tr
><tr
id=sl_svn41_301

><td class="source">        to the predecessor. Additionally, it removes the files from\<br></td></tr
><tr
id=sl_svn41_302

><td class="source">        the local Process.&quot;<br></td></tr
><tr
id=sl_svn41_303

><td class="source">        fileObjectList= []<br></td></tr
><tr
id=sl_svn41_304

><td class="source">        for subdir, dirs, files in os.walk(self._dir):<br></td></tr
><tr
id=sl_svn41_305

><td class="source">            for file in files:<br></td></tr
><tr
id=sl_svn41_306

><td class="source">                fileKey = self.assignHashKey(file)<br></td></tr
><tr
id=sl_svn41_307

><td class="source">                if self.isInRange(self._localClient.getKey(), self._predecessor.getKey(), fileKey):<br></td></tr
><tr
id=sl_svn41_308

><td class="source">                    fileObjectList.append(fileObject(file,fileKey))<br></td></tr
><tr
id=sl_svn41_309

><td class="source">                    os.remove(self._dir + &quot;/&quot; + file)<br></td></tr
><tr
id=sl_svn41_310

><td class="source">        #logging.debug(&quot;Returning file list of size {0} to predecessor&quot;.format(len(fileObjectList)))<br></td></tr
><tr
id=sl_svn41_311

><td class="source">        return fileObjectList<br></td></tr
><tr
id=sl_svn41_312

><td class="source">    <br></td></tr
><tr
id=sl_svn41_313

><td class="source">    def sendAllFiles(self):<br></td></tr
><tr
id=sl_svn41_314

><td class="source">        fileObjectList = []<br></td></tr
><tr
id=sl_svn41_315

><td class="source">        for subdir, dirs, files in os.walk(self._dir):<br></td></tr
><tr
id=sl_svn41_316

><td class="source">            for file in files:<br></td></tr
><tr
id=sl_svn41_317

><td class="source">                fileKey = self.assignHashKey(file)<br></td></tr
><tr
id=sl_svn41_318

><td class="source">                fileObjectList.append(fileObject(file,fileKey))<br></td></tr
><tr
id=sl_svn41_319

><td class="source">                os.remove(self._dir + &quot;/&quot; + file)<br></td></tr
><tr
id=sl_svn41_320

><td class="source">        self._successor.getAllFiles(fileObjectList)<br></td></tr
><tr
id=sl_svn41_321

><td class="source">        <br></td></tr
><tr
id=sl_svn41_322

><td class="source">         <br></td></tr
><tr
id=sl_svn41_323

><td class="source">    def getAllFiles(self,fileObjectList):<br></td></tr
><tr
id=sl_svn41_324

><td class="source">        self.writeFileObjectsToDisk(fileObjectList)<br></td></tr
><tr
id=sl_svn41_325

><td class="source">        return True<br></td></tr
><tr
id=sl_svn41_326

><td class="source">    <br></td></tr
><tr
id=sl_svn41_327

><td class="source">    def nodeLeave(self,leaveMode = &quot;voluntary&quot;):<br></td></tr
><tr
id=sl_svn41_328

><td class="source">        &quot;With this method, the current Client announces\<br></td></tr
><tr
id=sl_svn41_329

><td class="source">        its departure from the Chord ring, and all its files\<br></td></tr
><tr
id=sl_svn41_330

><td class="source">        are migrated to its successor.Returns TRUE on success&quot;<br></td></tr
><tr
id=sl_svn41_331

><td class="source">        if leaveMode == &quot;voluntary&quot;:<br></td></tr
><tr
id=sl_svn41_332

><td class="source">            if self._successor.getKey() != self._localClient.getKey():<br></td></tr
><tr
id=sl_svn41_333

><td class="source">                self.sendAllFiles()<br></td></tr
><tr
id=sl_svn41_334

><td class="source">        #logging.debug(&quot;Shutting down daemon&quot;)<br></td></tr
><tr
id=sl_svn41_335

><td class="source">        self._daemon.shutdown()<br></td></tr
><tr
id=sl_svn41_336

><td class="source">        #logging.debug(&quot;All Files sent to successor: {0} Got to go now....Bye Bye!&quot;.format(self._successor.getKey()))<br></td></tr
><tr
id=sl_svn41_337

><td class="source">        return True<br></td></tr
><tr
id=sl_svn41_338

><td class="source">    <br></td></tr
><tr
id=sl_svn41_339

><td class="source">    def createRing(self):<br></td></tr
><tr
id=sl_svn41_340

><td class="source">        &quot;This CHORD client instance is the first in the network&quot;<br></td></tr
><tr
id=sl_svn41_341

><td class="source">        self.predecessor = ChordProcessRecord()<br></td></tr
><tr
id=sl_svn41_342

><td class="source">        # The client is its own successor        <br></td></tr
><tr
id=sl_svn41_343

><td class="source">        self._successor   = ChordProcessRecord(self._localClient.getKey(),self._localClient.getPortNumber())<br></td></tr
><tr
id=sl_svn41_344

><td class="source">        self._successorList = [self._successor for item in  range(0,self.SUCCESSOR_LIST_SIZE)]<br></td></tr
><tr
id=sl_svn41_345

><td class="source">        return True<br></td></tr
><tr
id=sl_svn41_346

><td class="source"><br></td></tr
><tr
id=sl_svn41_347

><td class="source">    def stabilize(self):<br></td></tr
><tr
id=sl_svn41_348

><td class="source">        &quot;This method runs periodically on the client,\<br></td></tr
><tr
id=sl_svn41_349

><td class="source">        in order to learn about newly joined nodes.&quot;<br></td></tr
><tr
id=sl_svn41_350

><td class="source">        logging.debug(&quot;{0}:Stabilize &quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_351

><td class="source">        <br></td></tr
><tr
id=sl_svn41_352

><td class="source">        try:<br></td></tr
><tr
id=sl_svn41_353

><td class="source">            successorsPredecessor = self._successor.predecessor()<br></td></tr
><tr
id=sl_svn41_354

><td class="source">            if successorsPredecessor.isSet():<br></td></tr
><tr
id=sl_svn41_355

><td class="source">                logging.debug(&quot;{0} Stabilize:Got successor&#39;s predecessor: {1}&quot;.format(self._localClient.getKey(),successorsPredecessor.getKey()))<br></td></tr
><tr
id=sl_svn41_356

><td class="source">                if self.isInRange(self._localClient.getKey(),self._successor.getKey(),successorsPredecessor.getKey(),&quot;&gt;=&quot;):<br></td></tr
><tr
id=sl_svn41_357

><td class="source">                    logging.debug(&quot;{0}: Stabilize: Changing successor to {1}&quot;.format(self._localClient.getKey(),successorsPredecessor.getKey()))<br></td></tr
><tr
id=sl_svn41_358

><td class="source">                    self._successor = successorsPredecessor  <br></td></tr
><tr
id=sl_svn41_359

><td class="source">                    self._fingerTable[0] = self._successor<br></td></tr
><tr
id=sl_svn41_360

><td class="source">                <br></td></tr
><tr
id=sl_svn41_361

><td class="source">            self.fixSuccessorList()<br></td></tr
><tr
id=sl_svn41_362

><td class="source">            self._successor.notify(self._localClient)<br></td></tr
><tr
id=sl_svn41_363

><td class="source">            <br></td></tr
><tr
id=sl_svn41_364

><td class="source">            if self._successor.getKey() != self._localClient.getKey():<br></td></tr
><tr
id=sl_svn41_365

><td class="source">                fileObjectList = self._successor.getFiles()<br></td></tr
><tr
id=sl_svn41_366

><td class="source">                if fileObjectList != None:<br></td></tr
><tr
id=sl_svn41_367

><td class="source">                    self.writeFileObjectsToDisk(fileObjectList)<br></td></tr
><tr
id=sl_svn41_368

><td class="source">                <br></td></tr
><tr
id=sl_svn41_369

><td class="source">        except Pyro.errors.ProtocolError:<br></td></tr
><tr
id=sl_svn41_370

><td class="source">            logging.warning(&quot;{0}: Stabilize: Communication failed when trying to contact node {1}&quot;.format(self._localClient.getKey(),self._successor.getKey()))<br></td></tr
><tr
id=sl_svn41_371

><td class="source">            self.setNewSuccessor()<br></td></tr
><tr
id=sl_svn41_372

><td class="source">            <br></td></tr
><tr
id=sl_svn41_373

><td class="source">            <br></td></tr
><tr
id=sl_svn41_374

><td class="source">            <br></td></tr
><tr
id=sl_svn41_375

><td class="source">    def setNewSuccessor(self):<br></td></tr
><tr
id=sl_svn41_376

><td class="source">        &quot;After successor failure, a new successor must be\<br></td></tr
><tr
id=sl_svn41_377

><td class="source">        chosen from the successor list.Consequently the successor\<br></td></tr
><tr
id=sl_svn41_378

><td class="source">        list of the new successor must be chosen&quot;<br></td></tr
><tr
id=sl_svn41_379

><td class="source">        i=0<br></td></tr
><tr
id=sl_svn41_380

><td class="source">        while i &lt; len(self._successorList)\<br></td></tr
><tr
id=sl_svn41_381

><td class="source">            and isinstance(self._successorList[i],ChordProcessRecord)\<br></td></tr
><tr
id=sl_svn41_382

><td class="source">            and not self._successorList[i].isAlive():<br></td></tr
><tr
id=sl_svn41_383

><td class="source">            i = i + 1<br></td></tr
><tr
id=sl_svn41_384

><td class="source">            <br></td></tr
><tr
id=sl_svn41_385

><td class="source">        if i==len(self._successorList):<br></td></tr
><tr
id=sl_svn41_386

><td class="source">            return<br></td></tr
><tr
id=sl_svn41_387

><td class="source">            <br></td></tr
><tr
id=sl_svn41_388

><td class="source">        logging.debug(&quot;{0} setNewSuccessor: Due to successor failure, setting new successor to {1}&quot;.format(self._localClient.getKey(),self._successorList[i].getKey()))<br></td></tr
><tr
id=sl_svn41_389

><td class="source">        self._successor = self._successorList[i]<br></td></tr
><tr
id=sl_svn41_390

><td class="source">        self.fixSuccessorList()<br></td></tr
><tr
id=sl_svn41_391

><td class="source"><br></td></tr
><tr
id=sl_svn41_392

><td class="source">            <br></td></tr
><tr
id=sl_svn41_393

><td class="source">    def fixSuccessorList(self):<br></td></tr
><tr
id=sl_svn41_394

><td class="source">        &quot;Retrieve the successor list of the successor and\<br></td></tr
><tr
id=sl_svn41_395

><td class="source">        append it to the local successorList&quot;<br></td></tr
><tr
id=sl_svn41_396

><td class="source"><br></td></tr
><tr
id=sl_svn41_397

><td class="source">        successorsSucList = self._successor.getSuccessorList()  <br></td></tr
><tr
id=sl_svn41_398

><td class="source">        if successorsSucList != None:      <br></td></tr
><tr
id=sl_svn41_399

><td class="source">            sucLength = len(successorsSucList)<br></td></tr
><tr
id=sl_svn41_400

><td class="source">            self._successorList = [self._successor]<br></td></tr
><tr
id=sl_svn41_401

><td class="source">            self._successorList[1:sucLength] =  successorsSucList[0:sucLength-1] <br></td></tr
><tr
id=sl_svn41_402

><td class="source">            #logging.debug(&quot;FixSuccessorList:Got successor list from successor&quot;)<br></td></tr
><tr
id=sl_svn41_403

><td class="source">    <br></td></tr
><tr
id=sl_svn41_404

><td class="source">    def getSuccessorList(self):<br></td></tr
><tr
id=sl_svn41_405

><td class="source">        &quot;Getter for Successor list&quot;<br></td></tr
><tr
id=sl_svn41_406

><td class="source">        return self._successorList<br></td></tr
><tr
id=sl_svn41_407

><td class="source"><br></td></tr
><tr
id=sl_svn41_408

><td class="source">    <br></td></tr
><tr
id=sl_svn41_409

><td class="source">    def getNotified(self,predecessor):<br></td></tr
><tr
id=sl_svn41_410

><td class="source">        &quot;This method updates the successor&#39;s knowledge about\<br></td></tr
><tr
id=sl_svn41_411

><td class="source">        who is his predecessor.&quot;<br></td></tr
><tr
id=sl_svn41_412

><td class="source">        <br></td></tr
><tr
id=sl_svn41_413

><td class="source">        #logging.debug(&quot;getNotified:{0}: Predecessor notification by {1} &quot;.format(self._localClient.getKey(),predecessor.getKey()))<br></td></tr
><tr
id=sl_svn41_414

><td class="source">        if not self._predecessor.isSet():<br></td></tr
><tr
id=sl_svn41_415

><td class="source">            #logging.debug(&quot;getNotified:{0}: Notification:Changing predecessor to {1} &quot;.format(self._localClient.getKey(),predecessor.getKey()))<br></td></tr
><tr
id=sl_svn41_416

><td class="source">            self._predecessor = predecessor<br></td></tr
><tr
id=sl_svn41_417

><td class="source">        if self.isInRange(self._predecessor.getKey(), self._localClient.getKey(), predecessor.getKey(),&quot;&gt;=&quot;):<br></td></tr
><tr
id=sl_svn41_418

><td class="source">            #logging.debug(&quot;getNotified:{0}: Notification:IS IN RANGEChanging predecessor to {1} &quot;.format(self._localClient.getKey(),predecessor.getKey()))<br></td></tr
><tr
id=sl_svn41_419

><td class="source">            self._predecessor = predecessor<br></td></tr
><tr
id=sl_svn41_420

><td class="source">        <br></td></tr
><tr
id=sl_svn41_421

><td class="source">    def reportStatus(self):<br></td></tr
><tr
id=sl_svn41_422

><td class="source">        print(&quot;*********************************************************&quot;)<br></td></tr
><tr
id=sl_svn41_423

><td class="source">        print(&quot;*                  STATUS:                              *&quot;)<br></td></tr
><tr
id=sl_svn41_424

><td class="source">        print(&quot;* ------------------------------------------------------*&quot;)<br></td></tr
><tr
id=sl_svn41_425

><td class="source">        print(&quot;* Process Key= {0}                                  *&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_426

><td class="source">        print(&quot;* Successor  = {0}                                  *&quot;.format(self._successor.getKey()))<br></td></tr
><tr
id=sl_svn41_427

><td class="source">        print(&quot;* Predecessor= {0}                                     *&quot;.format(self._predecessor.getKey()))<br></td></tr
><tr
id=sl_svn41_428

><td class="source">        if self._fingerTableFull:<br></td></tr
><tr
id=sl_svn41_429

><td class="source">            entries = self.KEY_LENGTH<br></td></tr
><tr
id=sl_svn41_430

><td class="source">        else:<br></td></tr
><tr
id=sl_svn41_431

><td class="source">            entries = self._next  <br></td></tr
><tr
id=sl_svn41_432

><td class="source">        print(&quot;* Finger table entries: {0}                               *&quot;.format(entries))<br></td></tr
><tr
id=sl_svn41_433

><td class="source">        print(&quot;*********************************************************&quot;)<br></td></tr
><tr
id=sl_svn41_434

><td class="source">    <br></td></tr
><tr
id=sl_svn41_435

><td class="source">        <br></td></tr
><tr
id=sl_svn41_436

><td class="source">    def fixFingers(self):<br></td></tr
><tr
id=sl_svn41_437

><td class="source">        &quot;New nodes initialize their finger tables with\<br></td></tr
><tr
id=sl_svn41_438

><td class="source">        fixFingers and existing nodes incorporate new\<br></td></tr
><tr
id=sl_svn41_439

><td class="source">        nodes into their finger tables&quot;<br></td></tr
><tr
id=sl_svn41_440

><td class="source">        try:<br></td></tr
><tr
id=sl_svn41_441

><td class="source">            if self._next &gt;= self.KEY_LENGTH:<br></td></tr
><tr
id=sl_svn41_442

><td class="source">                self._next = 0<br></td></tr
><tr
id=sl_svn41_443

><td class="source">                self._fingerTableFull = True<br></td></tr
><tr
id=sl_svn41_444

><td class="source">            lookupKey = hex(int(self._localClient.getKey(),16) + 2**self._next)[2:]<br></td></tr
><tr
id=sl_svn41_445

><td class="source">            #logging.debug(&quot;fixFingers: Lookup key is {0}&quot;.format(lookupKey))<br></td></tr
><tr
id=sl_svn41_446

><td class="source">            self._fingerTable[self._next] = self.lookup(lookupKey)<br></td></tr
><tr
id=sl_svn41_447

><td class="source">            self._next = self._next + 1<br></td></tr
><tr
id=sl_svn41_448

><td class="source">            if(self._next == 32):<br></td></tr
><tr
id=sl_svn41_449

><td class="source">                print &quot;{0} :Finger table full&quot;.format(self._localClient.getKey())<br></td></tr
><tr
id=sl_svn41_450

><td class="source">            #logging.debug(&quot;fixFingers:Fixing finger position: {0} with key: {1}&quot;.format(self._next -1,self._fingerTable[self._next-1].getKey()))<br></td></tr
><tr
id=sl_svn41_451

><td class="source">        except Pyro.errors.ProtocolError:<br></td></tr
><tr
id=sl_svn41_452

><td class="source">            logging.warning(&quot;FixFingers: Communication failed&quot;)<br></td></tr
><tr
id=sl_svn41_453

><td class="source">        <br></td></tr
><tr
id=sl_svn41_454

><td class="source">    <br></td></tr
><tr
id=sl_svn41_455

><td class="source">    def callPeriodicFunctions(self):<br></td></tr
><tr
id=sl_svn41_456

><td class="source">        self.checkPredecessor()<br></td></tr
><tr
id=sl_svn41_457

><td class="source">        self.stabilize()    <br></td></tr
><tr
id=sl_svn41_458

><td class="source">        self.fixFingers()<br></td></tr
><tr
id=sl_svn41_459

><td class="source">        if not self._predecessor.isSet():<br></td></tr
><tr
id=sl_svn41_460

><td class="source">            self.reportStatus()<br></td></tr
><tr
id=sl_svn41_461

><td class="source">        <br></td></tr
><tr
id=sl_svn41_462

><td class="source">    def killChordProcess(self,signo,frame):<br></td></tr
><tr
id=sl_svn41_463

><td class="source">        print &quot;Caught signal!&quot;<br></td></tr
><tr
id=sl_svn41_464

><td class="source">        self._daemon.shutdown()<br></td></tr
><tr
id=sl_svn41_465

><td class="source">        exit()<br></td></tr
><tr
id=sl_svn41_466

><td class="source">      <br></td></tr
><tr
id=sl_svn41_467

><td class="source">    def checkPredecessor(self):<br></td></tr
><tr
id=sl_svn41_468

><td class="source">        &quot;Check whether the predecessor node\<br></td></tr
><tr
id=sl_svn41_469

><td class="source">        is alive and well.If not, set the predecessor\<br></td></tr
><tr
id=sl_svn41_470

><td class="source">        to a null Node&quot;<br></td></tr
><tr
id=sl_svn41_471

><td class="source">        if self._predecessor.isSet() and not self._predecessor.isAlive():<br></td></tr
><tr
id=sl_svn41_472

><td class="source">            logging.debug(&quot;{0} Predecessor is not responding.Setting predecessor to None&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_473

><td class="source">            self._predecessor = ChordProcessRecord()<br></td></tr
><tr
id=sl_svn41_474

><td class="source">              <br></td></tr
><tr
id=sl_svn41_475

><td class="source">            <br></td></tr
><tr
id=sl_svn41_476

><td class="source">    def getPredecessor(self):<br></td></tr
><tr
id=sl_svn41_477

><td class="source">        return self._predecessor<br></td></tr
><tr
id=sl_svn41_478

><td class="source">    <br></td></tr
><tr
id=sl_svn41_479

><td class="source">    def setBootstrapNode(self,port):<br></td></tr
><tr
id=sl_svn41_480

><td class="source">        self._bootstrapNodePort = port<br></td></tr
><tr
id=sl_svn41_481

><td class="source">        <br></td></tr
><tr
id=sl_svn41_482

><td class="source">    def setStatus(self,status):<br></td></tr
><tr
id=sl_svn41_483

><td class="source">        self._status = status<br></td></tr
><tr
id=sl_svn41_484

><td class="source">        <br></td></tr
><tr
id=sl_svn41_485

><td class="source">    def getStatus(self):<br></td></tr
><tr
id=sl_svn41_486

><td class="source">        return self._status<br></td></tr
><tr
id=sl_svn41_487

><td class="source">        <br></td></tr
><tr
id=sl_svn41_488

><td class="source">    def setPeriod(self,period):<br></td></tr
><tr
id=sl_svn41_489

><td class="source">        self.PERIOD = period<br></td></tr
><tr
id=sl_svn41_490

><td class="source">        <br></td></tr
><tr
id=sl_svn41_491

><td class="source">    def failure(self,signum, frame):<br></td></tr
><tr
id=sl_svn41_492

><td class="source">        &quot;Fail or respawn according to the churn rate&quot;<br></td></tr
><tr
id=sl_svn41_493

><td class="source">        if(random.random() &lt; self.CHURN_RATE):<br></td></tr
><tr
id=sl_svn41_494

><td class="source">            if self._status:<br></td></tr
><tr
id=sl_svn41_495

><td class="source">                if not self._controlProcess.notifyControl(self._localClient.getPortNumber(),False):<br></td></tr
><tr
id=sl_svn41_496

><td class="source">                    return<br></td></tr
><tr
id=sl_svn41_497

><td class="source">                print(&quot;{0} :Switching OFF daemon&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_498

><td class="source">                self._status = False<br></td></tr
><tr
id=sl_svn41_499

><td class="source">                self._daemon.shutdown()<br></td></tr
><tr
id=sl_svn41_500

><td class="source">            else:<br></td></tr
><tr
id=sl_svn41_501

><td class="source">                print(&quot;{0} :Switching ON daemon&quot;.format(self._localClient.getKey()))<br></td></tr
><tr
id=sl_svn41_502

><td class="source">                self._bootstrapNodePort =self._controlProcess.requestBootstrapNode()<br></td></tr
><tr
id=sl_svn41_503

><td class="source">                if self._bootstrapNodePort!=None:<br></td></tr
><tr
id=sl_svn41_504

><td class="source">                    thread.start_new_thread(self.localServer,())<br></td></tr
><tr
id=sl_svn41_505

><td class="source">                    self._status = True<br></td></tr
><tr
id=sl_svn41_506

><td class="source">                    <br></td></tr
><tr
id=sl_svn41_507

><td class="source">                self._controlProcess.notifyControl(self._localClient.getPortNumber(),True)<br></td></tr
><tr
id=sl_svn41_508

><td class="source">                     <br></td></tr
><tr
id=sl_svn41_509

><td class="source">        interval = int(math.ceil(random.expovariate(1)*6*self.PERIOD/self.CHURN_RATE))<br></td></tr
><tr
id=sl_svn41_510

><td class="source">#        print &quot;Interval is &quot;,interval<br></td></tr
><tr
id=sl_svn41_511

><td class="source">        if(interval &lt; self.MIN_EXP_TIME):<br></td></tr
><tr
id=sl_svn41_512

><td class="source">            interval = self.MIN_EXP_TIME<br></td></tr
><tr
id=sl_svn41_513

><td class="source">        signal.alarm(interval)<br></td></tr
><tr
id=sl_svn41_514

><td class="source">        <br></td></tr
><tr
id=sl_svn41_515

><td class="source">def main():<br></td></tr
><tr
id=sl_svn41_516

><td class="source">    &quot;Main function. Creates a server thread \<br></td></tr
><tr
id=sl_svn41_517

><td class="source">    and and puts the client in the Chord ring&quot;<br></td></tr
><tr
id=sl_svn41_518

><td class="source">    <br></td></tr
><tr
id=sl_svn41_519

><td class="source">    if len(sys.argv) !=4:<br></td></tr
><tr
id=sl_svn41_520

><td class="source">        print &quot;Usage: Process PortNumber BoostrapNode_Port Churn_Rate&quot;<br></td></tr
><tr
id=sl_svn41_521

><td class="source">        exit()<br></td></tr
><tr
id=sl_svn41_522

><td class="source">    <br></td></tr
><tr
id=sl_svn41_523

><td class="source">    # Create a new local instance ,4900 is the &quot;port&quot; of the master process   <br></td></tr
><tr
id=sl_svn41_524

><td class="source">    localClient = ChordProcess(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]),4900)<br></td></tr
><tr
id=sl_svn41_525

><td class="source"><br></td></tr
><tr
id=sl_svn41_526

><td class="source"><br></td></tr
><tr
id=sl_svn41_527

><td class="source">    #Start listening for control messages<br></td></tr
><tr
id=sl_svn41_528

><td class="source">    thread.start_new_thread(localClient.controlServer,())<br></td></tr
><tr
id=sl_svn41_529

><td class="source">        <br></td></tr
><tr
id=sl_svn41_530

><td class="source">    time.sleep(1)<br></td></tr
><tr
id=sl_svn41_531

><td class="source">    <br></td></tr
><tr
id=sl_svn41_532

><td class="source">    #Join the Chord ring via the bootstrap node<br></td></tr
><tr
id=sl_svn41_533

><td class="source">    localClient.nodeJoin()<br></td></tr
><tr
id=sl_svn41_534

><td class="source">    <br></td></tr
><tr
id=sl_svn41_535

><td class="source">    signal.signal(signal.SIGALRM, localClient.failure)<br></td></tr
><tr
id=sl_svn41_536

><td class="source">    if(localClient.CHURN_RATE!=0):<br></td></tr
><tr
id=sl_svn41_537

><td class="source">        signal.alarm(10)<br></td></tr
><tr
id=sl_svn41_538

><td class="source">    <br></td></tr
><tr
id=sl_svn41_539

><td class="source">    # Call periodic functions every PERIOD seconds        <br></td></tr
><tr
id=sl_svn41_540

><td class="source">    while(True):<br></td></tr
><tr
id=sl_svn41_541

><td class="source">        time.sleep(localClient.PERIOD)<br></td></tr
><tr
id=sl_svn41_542

><td class="source">        if localClient._status:<br></td></tr
><tr
id=sl_svn41_543

><td class="source">            localClient.callPeriodicFunctions()<br></td></tr
><tr
id=sl_svn41_544

><td class="source"><br></td></tr
><tr
id=sl_svn41_545

><td class="source">if __name__ == &quot;__main__&quot;:<br></td></tr
><tr
id=sl_svn41_546

><td class="source">    main()<br></td></tr
><tr
id=sl_svn41_547

><td class="source"><br></td></tr
><tr
id=sl_svn41_548

><td class="source"><br></td></tr
><tr
id=sl_svn41_549

><td class="source">    <br></td></tr
><tr
id=sl_svn41_550

><td class="source"><br></td></tr
><tr
id=sl_svn41_551

><td class="source"><br></td></tr
><tr
id=sl_svn41_552

><td class="source">    <br></td></tr
><tr
id=sl_svn41_553

><td class="source">        <br></td></tr
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
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=41&amp;format=side&amp;path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old_path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old=40">Diff</a>
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
 
 
 changed_paths.push('/trunk/ChordImplementation/src/Process/ChordProcessRecord.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ChordProcessRecord.py?r\x3d41\x26spec\x3dsvn41');
 
 
 changed_paths.push('/trunk/ChordImplementation/src/Process/ControlClass.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ControlClass.py?r\x3d41\x26spec\x3dsvn41');
 
 
 changed_paths.push('/trunk/ChordImplementation/src/Process/__init__.py');
 changed_urls.push('/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/__init__.py?r\x3d41\x26spec\x3dsvn41');
 
 var selected_path = '/trunk/ChordImplementation/src/Process/__init__.py';
 
 
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
 
 >...ion/src/ChordControl/__init__.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ChordProcessRecord.py?r=41&amp;spec=svn41"
 
 >...rc/Process/ChordProcessRecord.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/ControlClass.py?r=41&amp;spec=svn41"
 
 >...tion/src/Process/ControlClass.py</option>
 
 <option value="/p/chordimplementation/source/browse/trunk/ChordImplementation/src/Process/__init__.py?r=41&amp;spec=svn41"
 selected="selected"
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
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=40&amp;format=side&amp;path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old_path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old=39">Diff</a>
 <br>
 <pre class="ifOpened">[No log message]</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/chordimplementation/source/detail?spec=svn41&r=39">r39</a>
 by nassosantoniou
 on May 24, 2010
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=39&amp;format=side&amp;path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old_path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old=38">Diff</a>
 <br>
 <pre class="ifOpened">[No log message]</pre>
 </div>
 
 <div class="closed" style="margin-bottom:3px;" >
 <a class="ifClosed" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/plus.gif" ></a>
 <a class="ifOpened" onclick="return _toggleHidden(this)"><img src="https://ssl.gstatic.com/codesite/ph/images/minus.gif" ></a>
 <a href="/p/chordimplementation/source/detail?spec=svn41&r=38">r38</a>
 by dmitri.athanasiou
 on May 22, 2010
 &nbsp; <a href="/p/chordimplementation/source/diff?spec=svn41&r=38&amp;format=side&amp;path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old_path=/trunk/ChordImplementation/src/Process/__init__.py&amp;old=37">Diff</a>
 <br>
 <pre class="ifOpened">[No log message]</pre>
 </div>
 
 
 <a href="/p/chordimplementation/source/list?path=/trunk/ChordImplementation/src/Process/__init__.py&start=41">All revisions of this file</a>
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
 
 <div>Size: 23403 bytes,
 553 lines</div>
 
 <div><a href="//chordimplementation.googlecode.com/svn/trunk/ChordImplementation/src/Process/__init__.py">View raw file</a></div>
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
 var paths = {'svn41': '/trunk/ChordImplementation/src/Process/__init__.py'}
 codereviews = CR_controller.setup(
 {"projectName":"chordimplementation","loggedInUserEmail":"ethan.wjj@gmail.com","profileUrl":"/u/115244174812975043353/","assetHostPath":"https://ssl.gstatic.com/codesite/ph","token":"hsWkZbmZwW-OF1_Kq8EigbCaddk:1366668725836","assetVersionPath":"https://ssl.gstatic.com/codesite/ph/13714586478408612229","projectHomeUrl":"/p/chordimplementation","relativeBaseUrl":"","domainName":null}, '', 'svn41', paths,
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

