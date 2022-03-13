function Counter(props) {

    const filterAantal = props.selectedOffers;
    const totaalAantal = props.totalOffers;

    return (
        filterAantal + " /" + totaalAantal
    )
}

export default Counter;
  