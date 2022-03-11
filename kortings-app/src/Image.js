function Image(props) {

    const image = props.image;

    return (
        <span className="product-image">
            <img alt='' src={image}/>
        </span>
    )
}

export default Image;
  