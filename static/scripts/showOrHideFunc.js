// 全局变量，用于保证仅有一个区域/功能可见
function allInvisible() {
    const areas = ['customerTable', 'trainerTable', 'insertCustomer', 'searchCustomer'];
    areas.forEach(area => {
        const element = document.getElementById(area);
        if (element) {
            element.style.display = 'none';
        }
    });
}

// 设置customer table 是否可见
function customerTableVisibility() {
    allInvisible();
    const customerTable = document.getElementById('customerTable');
    if (customerTable) {
        customerTable.style.display = 'block';
    }
}

// 设置trainer table 是否可见
function trainerTableVisibility() {
    allInvisible();
    const trainerTable = document.getElementById('trainerTable');
    if (trainerTable) {
        trainerTable.style.display = 'block';
    }
}

// 设置insert customer 是否可见
function insertCustomerVisibility() {
    allInvisible();
    const insertCustomer = document.getElementById('insertCustomer');
    if (insertCustomer) {
        insertCustomer.style.display = 'block';
    }
}

// 设置search customer 是否可见
function searchCustomerVisibility() {
    allInvisible();
    const searchCustomer = document.getElementById('searchCustomer');
    if (searchCustomer) {
        searchCustomer.style.display = 'block';
    }
}