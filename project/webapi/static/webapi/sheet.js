/**
 * Created by scott on 2016/10/9.
 */
$(function() {


	$('#btn_sheet_new').click(function(){
		var m = $('#list_module').datagrid('getSelected');
		if( m == null){
			$.messager.alert("warning","you should select one module row!");
			return;
		}
		$('#dlg_sheet').window({
			title:'New Sheet ..',
			width:800,
			//height:500,
			modal:true
		});

		$('#dlg_sheet').data('module',m).window('refresh','/static/webapi/sheet_info.html');
	});

});
