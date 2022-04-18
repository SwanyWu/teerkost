import localForage from 'localforage'

function ProductBookmark(props) {

    const productId = props.id;

    const triggerButtonAnimation = () => {

        const element = document.querySelector('.personal-list-button')

        element.classList.remove('jumpy'); // reset animation
        void element.offsetWidth; // trigger reflow
        element.classList.add('jumpy'); // start animation
    }

    const triggerButtonUpdate = () => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            var amount = 0
            if(value !== null) {
                amount = value.length
            }
            const element = document.querySelector('.personal-list-button-tag')
            element.textContent = amount    
        }) 
    }

    const registerBookmark = (id) => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            if(value !== null) { // if something is present in browserstorage
                const valueFound = value.find(element => element === id)

                if(valueFound === id) {
                    console.log("bestaat al")
                    // FIXME id weggooien in dit geval?
                } else {
                    var allBookmarks = value;
                    allBookmarks.push(id) // push to the existing array
        
                    localForage.setItem('teerkost-bookmarks', allBookmarks).then(function(value) {
                        console.log("De array " + value + " is toegevoegd")
                        triggerButtonAnimation()
                        triggerButtonUpdate()
                    }).catch(function (err) {
                        console.log("Iets misgegaan bij het opslaan van bookmark: " + err)
                    })
                }
            } else {
                var allBookmarks = [id] // nothing found, make a new array with first id
                console.log("niks gevonden. Tijd om te starten")
                localForage.setItem('teerkost-bookmarks', allBookmarks).then(function(value) {
                    console.log("Voor het eerst, de array " + value + " toegevoegd")
                }).catch(function (err) {
                    console.log("Iets misgegaan bij het opslaan van eerste bookmark: " + err)
                })
            }
        }).catch(function(err) {
            console.log("Iets misgegaan bij het ophalen van data: " + err)
        })
    }

    const getCorrectBookmarkIcon = (productId) => {
        localForage.getItem('teerkost-bookmarks').then(function (value) {
            if(value !== null) { // if something is present in browserstorage
                const valueFound = value.find(element => element === productId)
                if(valueFound === productId) {
                    return "ja"
                    // return <i class='ri-bookmark-line'></i>
                } else {
                    return "nee"
                }
            } else {
                return "aaaa"
            }
        })
        return <i class='ri-bookmark-line'></i>
    }

    return (
        <span onClick={() => registerBookmark(productId)} className="product-bookmark">{getCorrectBookmarkIcon(productId)}</span>
    )

}

export default ProductBookmark;