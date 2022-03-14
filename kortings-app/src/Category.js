function Category(props) {

    const category = props.category;

    if(category !== "") {
        return (
            <span className="product-category">{category}</span> 
        )
    }
    else {
        return (<span></span>)
    }
}

export default Category;
  