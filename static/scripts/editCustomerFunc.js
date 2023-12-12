// 打开模态窗
function openCustomerEditModal(button) {
    // 使用按钮中的数据填充模态
    const trElement = button.closest('tr');
    const customerId = trElement.getAttribute('data-customer-id');
    document.getElementById('editCustomerModal').setAttribute('data-customer-id', customerId);
    document.getElementById('edit_customer_first_name').value = trElement.getAttribute('data-first-name');
    document.getElementById('edit_customer_last_name').value = trElement.getAttribute('data-last-name');
    document.getElementById('edit_customer_address').value = trElement.getAttribute('data-address');
    document.getElementById('edit_customer_phone').value = trElement.getAttribute('data-phone');
    document.getElementById('edit_customer_email').value = trElement.getAttribute('data-email');
    document.getElementById('edit_customer_birthdate').value = trElement.getAttribute('data-birthdate');
    document.getElementById('edit_customer_exercise_history').value = trElement.getAttribute('data-exercise_history');
    document.getElementById('edit_customer_fitness_level').value = trElement.getAttribute('data-fitness_level');
    document.getElementById('edit_customer_medical_history').value = trElement.getAttribute('data-medical_history');
    // 显示模态窗
    document.getElementById('editCustomerModal').style.display = 'block';
}
// 更新客户信息
function updateCustomer() {
    // 从表单中收集更新的数据
    // noinspection SpellCheckingInspection
    const updatedData = {
        firstname: document.getElementById('edit_customer_first_name').value,
        lastname: document.getElementById('edit_customer_last_name').value,
        address: document.getElementById('edit_customer_address').value,
        phone: document.getElementById('edit_customer_phone').value,
        email: document.getElementById('edit_customer_email').value,
        birthdate: document.getElementById('edit_customer_birthdate').value,
        exercisehistory: document.getElementById('edit_customer_exercise_history').value,
        fitnesslevel: document.getElementById('edit_customer_fitness_level').value,
        medicalhistory: document.getElementById('edit_customer_medical_history').value
    };
    // 获取当前客户的ID
    const customerId = document.getElementById('editCustomerModal').getAttribute('data-customer-id');
    // 发起 fetch 请求，将客户ID作为URL参数传递
    fetch('/updateCustomer/' + customerId, {
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
        window.location.href = '/customer';
    })
    .catch(error => {
        // 处理错误
        console.error('更新失败：', error);
    });
    // 在启动更新后关闭模态框
    closeEditCustomerModal();
}
//关闭编辑模态框
function closeEditCustomerModal() {
    document.getElementById('editCustomerModal').style.display = 'none';
}

