document.getElementById('schedule-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const eventName = document.getElementById('event').value;
    const eventDate = document.getElementById('date').value;

    if (eventName && eventDate) {
        addSchedule(eventName, eventDate);
        document.getElementById('event').value = '';
        document.getElementById('date').value = '';
    }
});

function addSchedule(name, date) {
    const scheduleList = document.getElementById('schedule-list');
    const listItem = document.createElement('li');
    listItem.textContent = `${name} - ${date}`;
    
    scheduleList.appendChild(listItem);
    
    saveSchedule(name, date);
}

function saveSchedule(name, date) {
    const schedules = JSON.parse(localStorage.getItem('schedules')) || [];
    schedules.push({ name, date });
    localStorage.setItem('schedules', JSON.stringify(schedules));
}

function loadSchedules() {
    const schedules = JSON.parse(localStorage.getItem('schedules')) || [];
    schedules.forEach(schedule => addSchedule(schedule.name, schedule.date));
}

// 초기 로드 시 일정 로드
document.addEventListener('DOMContentLoaded', function() {
    loadSchedules();
});
