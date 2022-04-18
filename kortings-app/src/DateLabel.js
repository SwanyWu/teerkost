function DateLabel(props) {

    const todaysDateString = () => {
        const today = new Date();
        const dateNowString = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
        return dateNowString;
    }

    const returnDayAndMonth = (dateProp) => {
        const datestamp = dateProp.split("-");
        var day = datestamp[2];

        var allMonths = ['jan', 'feb', 'mrt', 'apr', 'mei', 'jun', 'jul', 'aug', 'sept', 'okt', 'nov', 'dec'];
        var month = allMonths[datestamp[1] - 1];
        return { day, month };
    }

    if(props !== undefined) {
        var dateNowParsed = Date.parse(todaysDateString())

        if(props.dateEnd !== "") {
            var dateEndParsed = Date.parse(props.dateEnd)
            var { day: dayEnd, month: monthEnd } = returnDayAndMonth(props.dateEnd);
        }
        var { day: dayStart, month: monthStart } = returnDayAndMonth(props.dateStart);
        var dateStartParsed = Date.parse(props.dateStart)

        if(dateStartParsed > dateNowParsed) {
            return (
                <span className="product-date">
                {"vanaf " + parseInt(dayStart, 10) + " " + monthStart}
                </span> 
            )          
        }
        else if(dateStartParsed === dateNowParsed) {
            return (
                <span className="product-date">
                {"vanaf vandaag"}
                </span> 
            )              
        }
        else {
            if(props.dateEnd !== "") {
                if(dateEndParsed === dateNowParsed) {
                    return (
                        <span className="product-date date-now">
                            {"tot vandaag"}
                        </span>
                    )
                }
                else if(dateEndParsed < dateNowParsed) {
                    return (
                        <span className="product-date date-now">
                            {"tot " + parseInt(dayEnd, 10) + " " + monthEnd}
                        </span>
                    )                    
                }
                else {
                    return (
                        <span className="product-date">
                            {" t/m " + parseInt(dayEnd, 10) + " " + monthEnd}
                        </span>
                    )
                }
            }
            else {
                return ( "" )
            }

        }
    }
 
}

export default DateLabel;
