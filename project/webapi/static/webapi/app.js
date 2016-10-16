/**
 * Created by scott on 2016/10/8.
 */
$(function(){

	$('#btn_app_new').click(function(){
		$('#dlg_app').dialog({
			title:'New Application ..',
			width:600,
			//height:500,
			modal:true
		});
		$('#dlg_app').data('app',null).dialog('refresh','/static/webapi/app_info.html');
	});

	$('#btn_app_edit').click(function(){
		var app = $('#list_app').datagrid('getSelected');
		if(app!=null) {
			$('#dlg_app').dialog(
				{
					title: 'Edit Application ..',
					width: 600,
					modal: true
				});
			$('#dlg_app').data('app', app).dialog('refresh', '/static/webapi/app_info.html');
		}else {
			$.messager.alert("Warning","please select one app row!");
		}
	});

	$('#btn_app_del').click(function(){
		var app = $('#list_app').datagrid('getSelected');
		if(app!=null) {
			$.messager.confirm('Confirm', 'you will delete this row ,really?', function(r){
				if (!r){
					return ;
				}

				$.ajax({
					url:'/webapi/applications/'+app.id + '/',
					method: 'delete',
					success:function(data){
						if( data.status == 0) {
							$('#list_app').datagrid('reload');
						}else{
							$.messager.alert('error', 'error:'+ data.errcode );
						}

					},
					error:function(xhr,status,error){
						$.messager.alert('error', status + error);
					}
				});
			});

		}else {
			$.messager.alert("Warning","please select one app row!");
		}
	});

});

