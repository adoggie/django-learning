/**
 * Created by scott on 2016/10/10.
 */


	function UUID() {
	  var s = [];
	  var hexDigits = "0123456789abcdef";
	  for (var i = 0; i < 36; i++) {
	    s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
	  }
	  s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
	  s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
	  s[8] = s[13] = s[18] = s[23] = "_";

	  var uuid = s.join("");
	  return uuid;
	}

	$.extend($.fn.datagrid.methods, {
			editCell: function(jq,param){
				return jq.each(function(){
					var opts = $(this).datagrid('options');
					var fields = $(this).datagrid('getColumnFields',true).concat($(this).datagrid('getColumnFields'));
					for(var i=0; i<fields.length; i++){
						var col = $(this).datagrid('getColumnOption', fields[i]);
						col.editor1 = col.editor;
						if (fields[i] != param.field){
							col.editor = null;
						}
					}
					$(this).datagrid('beginEdit', param.index);
					var ed = $(this).datagrid('getEditor', param);
					if (ed){
						if ($(ed.target).hasClass('textbox-f')){
							$(ed.target).textbox('textbox').focus();
						} else {
							$(ed.target).focus();
						}
					}
					for(var i=0; i<fields.length; i++){
						var col = $(this).datagrid('getColumnOption', fields[i]);
						col.editor = col.editor1;
					}
				});
			},
			enableCellEditing: function(jq){
				return jq.each(function(){
					var dg = $(this);
					var opts = dg.datagrid('options');
					opts.oldOnClickCell = opts.onClickCell;
					opts.onClickCell = function(index, field){
						if (opts.editIndex != undefined){
							if (dg.datagrid('validateRow', opts.editIndex)){
								dg.datagrid('endEdit', opts.editIndex);
								opts.editIndex = undefined;
							} else {
								return;
							}
						}
						dg.datagrid('selectRow', index).datagrid('editCell', {
							index: index,
							field: field
						});
						opts.editIndex = index;
						opts.oldOnClickCell.call(this, index, field);
					}
				});
			}
	});
	//-------------------------
	$.extend($.fn.treegrid.methods, {
			editCell: function(jq,param){
				return jq.each(function(){
					var opts = $(this).treegrid('options');
					var fields = $(this).treegrid('getColumnFields',true).concat($(this).treegrid('getColumnFields'));
					for(var i=0; i<fields.length; i++){
						var col = $(this).treegrid('getColumnOption', fields[i]);
						col.editor1 = col.editor;
						if (fields[i] != param.field){
							col.editor = null;
						}
					}
					$(this).treegrid('beginEdit', param.id);
					var ed = $(this).treegrid('getEditor', param);
					if (ed){
						if ($(ed.target).hasClass('textbox-f')){
							$(ed.target).textbox('textbox').focus();
						} else {
							$(ed.target).focus();
						}
					}
					for(var i=0; i<fields.length; i++){
						var col = $(this).treegrid('getColumnOption', fields[i]);
						col.editor = col.editor1;
					}
				});
			},
			enableCellEditing: function(jq){
				return jq.each(function(){
					var dg = $(this);

					var opts = dg.treegrid('options');
					opts.oldOnClickCell = opts.onClickCell;

					opts.onClickCell = function(index, field){

						if (opts.editIndex != undefined){
							if (dg.treegrid('validateRow', opts.editIndex)){
								dg.treegrid('endEdit', opts.editIndex);
								opts.editIndex = undefined;
							} else {
								return;
							}
						}
						dg.treegrid('select', field.id).treegrid('editCell', {
							id: field.id,
							field: index,
						});
						opts.editIndex = field.id;
						opts.oldOnClickCell.call(this, index, field);

					}
				});
			},
			stopCellEditing: function(jq){
				return jq.each(function(){
					var dg = $(this);
					var opts = dg.treegrid('options');
					if (opts.editIndex != undefined){
						if (dg.treegrid('validateRow', opts.editIndex)){
							dg.treegrid('endEdit', opts.editIndex);
							opts.editIndex = undefined;
						} else {
							return;
						}
					}
				});
			}
	});
