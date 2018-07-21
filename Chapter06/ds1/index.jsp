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
    <title>jndi 例子</title>
  </head>  
  <body> 
    <%
	    ///初始化上下文
    	Context ctx = new InitialContext();
		// 查找JDNI数据源 jdbc/mysql
    	DataSource ds = (DataSource)ctx.lookup("jdbc/mysql");
		// 从数据源中获得数据库连接句柄
    	Connection conn = ds.getConnection();
    	PreparedStatement ps = conn.prepareStatement("select count(*) from user");
    	ResultSet rs = ps.executeQuery();
    	if (rs.next()) {
    		out.print("学生记录总数为:" + rs.getInt(1));
    	}
    	conn.close();
    	ps.close();
    	rs.close();
     %>
  </body>
</html>
