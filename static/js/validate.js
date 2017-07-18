 $('.car').on('click', function () {
			
			
	var real_name = $('input[name="realname"]').val();
	var country = $('input[name="country"]').val();
	var type = $('input[name="type"]').val();
	var major = $('input[name="major"]').val();
	
	if (real_name == '' || country == '' || type == '' || major == ''){
		layer.open({
		  title: '西柚留学网提示'
		  ,content: '您有选项未填写,请全部填写完整！'
		});
		return false;
	}

	$.ajax({
		cache: false,
		type: "POST",
		url:"{% url 'user:highapply' %}",
		data:{'real_name':real_name, 'country':country, 'type':type, 'major':major},
		async: true,
		beforeSend:function(xhr, settings){
			xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
		},
		success: function(data) {
			if(data.status == 'fail'){
				layer.open({
				  title: '西柚留学网提示'
				  ,content: '申请失败，请稍后再试！'
				});
			}else if(data.status == 'success'){
				layer.open({
				  title: '西柚留学网提示'
				  ,content: '申请成功，稍后工作人员会与您联系！'
				});
			}
		},
	});

	return false;

})