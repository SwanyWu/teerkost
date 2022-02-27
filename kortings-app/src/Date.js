function Date(props) {
    if(props.dateEnd !== "") {
        var { day: dayEnd, month: monthEnd } = returnDayAndMonth(props.dateEnd);

        if(props.dateStart !== "") {
            var { day: dayStart, month: monthStart } = returnDayAndMonth(props.dateStart);

            return (
                <span className="product-date-start">
                    {"" + parseInt(dayStart, 10) + " " + monthStart}
                    {" t/m " + parseInt(dayEnd, 10) + " " + monthEnd}
                </span>
            )
        }
        else {
            return (
                <span className="product-date-end">{" " + parseInt(dayEnd, 10) + " " + monthEnd}</span>
            )
        }

    }
    else {
        return (
            ""
        )
    }   

    function returnDayAndMonth(dateProp) {
        const datestamp = dateProp.split("-");
        var day = datestamp[2];

        var allMonths = ['jan', 'feb', 'mrt', 'apr', 'mei', 'jun', 'jul', 'aug', 'sept', 'okt', 'nov', 'dec'];
        var month = allMonths[datestamp[1] - 1];
        return { day, month };
    }
}

export default Date;