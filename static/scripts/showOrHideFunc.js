// 全局变量，用于保证仅有一个区域/功能可见
function allInvisible() {
    const areas = ['Customer', 'customerTable', 'insertCustomer', 'searchCustomer',
                            'Trainer', 'trainerTable', 'insertTrainer', 'searchTrainer',
                            'Transaction', 'transactionTable', 'insertTransaction', 'searchTransaction',
                            'overAge', 'overAgeResult', 'fitGold', 'clientNumber', 'moneyReport'];
    areas.forEach(area => {
        const element = document.getElementById(area);
        if (element) {
            element.style.display = 'none';
        }
    });
}
// 设置customer是否可见
function customerVisibility() {
    allInvisible();
    const customer = document.getElementById('Customer');
    if (customer) {
        customer.style.display = 'block';
    }
}
// 设置customer table是否可见
function customerTableVisibility() {
    allInvisible();
    customerVisibility();
    const customerTable = document.getElementById('customerTable');
    if (customerTable) {
        customerTable.style.display = 'block';
    }
}
// 设置insert customer是否可见
function insertCustomerVisibility() {
    allInvisible();
    customerVisibility();
    const insertCustomer = document.getElementById('insertCustomer');
    if (insertCustomer) {
        insertCustomer.style.display = 'block';
    }
}
// 设置search customer是否可见
function searchCustomerVisibility() {
    allInvisible();
    customerVisibility();
    const searchCustomer = document.getElementById('searchCustomer');
    if (searchCustomer) {
        searchCustomer.style.display = 'block';
    }
}

// 设置trainer是否可见
function trainerVisibility() {
    allInvisible();
    const trainer = document.getElementById('Trainer');
    if (trainer) {
        trainer.style.display = 'block';
    }
}

// 设置trainer table 是否可见
function trainerTableVisibility() {
    allInvisible();
    trainerVisibility();
    const trainerTable = document.getElementById('trainerTable');
    if (trainerTable) {
        trainerTable.style.display = 'block';
    }
}
// 设置 insert trainer 是否可见
function insertTrainerVisibility() {
    allInvisible();
    trainerVisibility();
    const insertTrainer = document.getElementById('insertTrainer');
    if (insertTrainer) {
        insertTrainer.style.display = 'block';
    }
}
// 设置 search trainer 是否可见
function searchTrainerVisibility() {
    allInvisible();
    trainerVisibility();
    const searchTrainer = document.getElementById('searchTrainer');
    if (searchTrainer) {
        searchTrainer.style.display = 'block';
    }
}

// 设置transaction是否可见
function transactionVisibility() {
    allInvisible();
    const transaction = document.getElementById('Transaction');
    if (transaction) {
        transaction.style.display = 'block';
    }
}

// 设置transaction table 是否可见
function transactionTableVisibility() {
    allInvisible();
    transactionVisibility();
    const transactionTable = document.getElementById('transactionTable');
    if (transactionTable) {
        transactionTable.style.display = 'block';
    }
}

// 设置 insert transaction是否可见
function insertTransactionVisibility() {
    allInvisible();
    transactionVisibility();
    const insertTransaction = document.getElementById('insertTransaction');
    if (insertTransaction) {
        insertTransaction.style.display = 'block';
    }
}
// 设置 search transaction 是否可见
function searchTransactionVisibility() {
    allInvisible();
    transactionVisibility();
    const searchTransaction = document.getElementById('searchTransaction');
    if (searchTransaction) {
        searchTransaction.style.display = 'block';
    }
}

//设置over an age 功能是否可见
function overAgeVisibility(){
    allInvisible();
    const overAge = document.getElementById('overAge');
    if (overAge) {
        overAge.style.display = 'block';
    }
    const overAgeResult = document.getElementById('overAgeResult');
    if (overAgeResult) {
        overAgeResult.style.display = 'block';
    }
}
//设置fit and gold 功能是否可见
function fitGoldVisibility(){
    allInvisible();
    const fitGold = document.getElementById('fitGold');
    if (fitGold) {
        fitGold.style.display = 'block';
    }
}

function clientNumberVisibility(){
    allInvisible();
    const clientNumber = document.getElementById('clientNumber');
    if (clientNumber) {
        clientNumber.style.display = 'block';
    }
}
function moneyReportVisibility(){
    allInvisible();
    const moneyReport = document.getElementById('moneyReport');
    if (moneyReport) {
        moneyReport.style.display = 'block';
    }
}