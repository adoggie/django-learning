/**
 * Created by scott on 2016/10/8.
 */
$(function(){

	$('#btn_m_new').click(function(){
		var app = $('#list_app').datagrid('getSelected');
		if( app == null){
			$.messager.alert("warning","you shuld select one app row!");
			return;
		}
		$('#dlg_module').dialog({
			title:'New Module ..',
			width:600,
			//height:500,
			modal:true
		});

		$('#dlg_module').data('app',app).
		data('module',null).dialog('refresh','/static/webapi/module_info.html');
	});

	$('#btn_m_edit').click(function(){
		var module = $('#list_module').datagrid('getSelected');
		if( module !=null) {
			$('#dlg_module').dialog(
				{
					title: 'Edit Module ..',
					width: 600,
					modal: true
				});
			$('#dlg_module').data('module', module).dialog('refresh', '/static/webapi/module_info.html');
		}else {
			$.messager.alert("Warning","please select one app row!");
		}
	});

});

