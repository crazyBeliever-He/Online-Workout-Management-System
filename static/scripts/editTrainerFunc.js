// 打开模态窗
function openTrainerEditModal(button) {
    // 使用按钮中的数据填充模态
    const trElement = button.closest('tr');
    const trainerId = trElement.getAttribute('data-trainer-id');
    document.getElementById('editTrainerModal').setAttribute('data-trainer-id', trainerId);
    document.getElementById('edit_trainer_first_name').value = trElement.getAttribute('data-first-name');
    document.getElementById('edit_trainer_last_name').value = trElement.getAttribute('data-last-name');
    document.getElementById('edit_trainer_address').value = trElement.getAttribute('data-address');
    document.getElementById('edit_trainer_phone').value = trElement.getAttribute('data-phone');
    document.getElementById('edit_trainer_email').value = trElement.getAttribute('data-email');
    // 显示模态窗
    document.getElementById('editTrainerModal').style.display = 'block';
}
// 更新客户信息
function updateTrainer() {
    // 从表单中收集更新的数据
    // noinspection SpellCheckingInspection
    const updatedData = {
        firstname: document.getElementById('edit_trainer_first_name').value,
        lastname: document.getElementById('edit_trainer_last_name').value,
        address: document.getElementById('edit_trainer_address').value,
        phone: document.getElementById('edit_trainer_phone').value,
        email: document.getElementById('edit_trainer_email').value,
    };
    // 获取当前客户的ID
    console.log('dddd',updatedData);
    const trainerId = document.getElementById('editTrainerModal').getAttribute('data-trainer-id');
    // 发起 fetch 请求，将客户ID作为URL参数传递
    fetch('/updateTrainer/' + trainerId, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedData),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // 处理成功响应的数据
        console.log('更新成功！',data);
        // 刷新页面
        window.location.href = '/trainer';
    })
    .catch(error => {
        // 处理错误
        console.error('更新失败：', error);
    });
    // 在启动更新后关闭模态框
    closeEditTrainerModal();
}
//关闭编辑模态框
function closeEditTrainerModal() {
    document.getElementById('editTrainerModal').style.display = 'none';
}

