<%@ page language="java" contentType="text/html; charset=utf-8"
	pageEncoding="utf-8"%>	
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.Connection"%>
<%@page import="javax.sql.DataSource"%>
<%@page import="javax.naming.InitialContext"%>
<%@page import="javax.naming.Context"%>

<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
%>

<!DOCTYPE HTML>
<html>
  <head>
    <base href="<%=basePath%>">
    
    <title>My JSP 'index.jsp' starting page</title>
	<meta http-equiv="pragma" content="no-cache">
	<meta http-equiv="cache-control" content="no-cache">
	<meta http-equiv="expires" content="0">    
	<meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
	<meta http-equiv="description" content="This is my page">
	<!--
	<link rel="stylesheet" type="text/css" href="styles.css">
	-->
  </head>
  
  <body>
    This is my JSP page. <br>
    <%
    	Context ctx = new InitialContext();
    	DataSource ds = (DataSource)ctx.lookup("jdbc/mysql");
    	Connection conn = ds.getConnection();
    	PreparedStatement ps = conn.prepareStatement("select count(*) from user");
    	ResultSet rs = ps.executeQuery();
    	if (rs.next()) {
    		out.print("total:" + rs.getInt(1));
    	}
    	conn.close();
    	ps.close();
    	rs.close();
     %>
  </body>
</html>
