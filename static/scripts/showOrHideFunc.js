// 全局变量，用于保证仅有一个区域/功能可见
function allInvisible() {
    const areas = ['customerTable', 'insertCustomer', 'searchCustomer', 'trainerTable', 'insertTrainer',
                            'searchTrainer', 'transactionTable', 'insertTransaction', 'searchTransaction',
                            'overAge', 'overAgeResult', 'fitGold', 'clientNumber', 'moneyReport'];
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

// 设置customer function 是否可见
function customerFunctionVisibility() {
    allInvisible();
    const insertCustomer = document.getElementById('insertCustomer');
    if (insertCustomer) {
        insertCustomer.style.display = 'block';
    }
    const searchCustomer = document.getElementById('searchCustomer');
    if (searchCustomer) {
        searchCustomer.style.display = 'block';
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

// 设置 trainer function 是否可见
function trainerFunctionVisibility() {
    allInvisible();
    const insertTrainer = document.getElementById('insertTrainer');
    if (insertTrainer) {
        insertTrainer.style.display = 'block';
    }
    const searchTrainer = document.getElementById('searchTrainer');
    if (searchTrainer) {
        searchTrainer.style.display = 'block';
    }
}

// 设置transaction table 是否可见
function transactionTableVisibility() {
    allInvisible();
    const transactionTable = document.getElementById('transactionTable');
    if (transactionTable) {
        transactionTable.style.display = 'block';
    }
}

// 设置 transaction function 是否可见
function transactionFunctionVisibility() {
    allInvisible();
    const insertTransaction = document.getElementById('insertTransaction');
    if (insertTransaction) {
        insertTransaction.style.display = 'block';
    }
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