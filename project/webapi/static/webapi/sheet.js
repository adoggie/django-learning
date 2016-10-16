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
		$('#dlg_sheet').data('data',{action:'new',sheet_id:null,module_id:m.id}).window('refresh','/static/webapi/sheet_info.html');
	});

	$('#btn_sheet_copy').click(function(){
		var selitem = $('#list_sheet').datagrid('getSelected');
		if( selitem == null ) {
			$.messager.alert('warning','please select one sheet row!');
			return ;
		}
		var m = $('#list_module').datagrid('getSelected');
		if( m == null){
			$.messager.alert("warning","you should select one module row!");
			return;
		}

		$('#dlg_sheet').window({
			title:'New Sheet ..',
			width:800,
			modal:true
		});
		$('#dlg_sheet').data('data',{action:'copy',sheet_id:selitem.id,module_id:m.id}).window('refresh','/static/webapi/sheet_info.html');
	});

	$('#btn_sheet_edit').click(function(){
		var selitem = $('#list_sheet').datagrid('getSelected');
		if( selitem == null ) {
			$.messager.alert('warning','please select one sheet row!');
			return ;
		}
		$('#dlg_sheet').window({
			title:'New Sheet ..',
			width:800,
			modal:true
		});
		$('#dlg_sheet').data('data',{action:'edit',sheet_id:selitem.id}).window('refresh','/static/webapi/sheet_info.html');

	});

	$('#btn_sheet_del').click(function(){
		var selitems = $('#list_sheet').datagrid('getSelections');
		if( selitems.length ==0 ) {
			$.messager.alert('warning','please select one sheet row!');
			return ;
		}
		for( var item in selitems ) {
			$.ajax({
				url: '/webapi/sheets/' + item.id + '/',
				method: 'delete',
				success:function(data){
					if( data.status !=0){
						$.messager.alert('error','error:' + data.errcode + ' errmsg:'+ data.errmsg);
						return ;
					}
					$('#list_sheet').datagrid('reload');
				}
			});
		}

	});




});
