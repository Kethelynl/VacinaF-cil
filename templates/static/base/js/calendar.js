document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'pt-br',
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        events: '/api/user-vaccines/',
        eventColor: '#3788d8',
        eventTextColor: '#ffffff',
        height: 'auto',
        dayMaxEvents: true,
        selectable: true,
    });
    
    calendar.render();

    // Adiciona um listener para redimensionamento
    window.addEventListener('resize', function() {
        calendar.updateSize();
    });
});