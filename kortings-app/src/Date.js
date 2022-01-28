function Date(props) {

    const datestamp = props.dateEnd.split("-");
    var year = datestamp[0]
    var day = datestamp[2]

    var allMonths = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'];
    var month = allMonths[datestamp[1]-1]

    return (
          <span className="product-date-end">{" " + parseInt(day, 10) + " " + month}</span>
    )
        
}

export default Date;
  