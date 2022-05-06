import ShareDialog from "../components/ShareDialog";
import GoHomeButton from "../GoHomeButton";
import BookmarkButton from "../BookmarkButton";
import ShareButton from "../ShareButton";

function NoBookmarks() {
    return (
      <div className="app-wrap">
        <ShareDialog customUrl="https://teerkost.nl/#/bewaard" buttonText="deel pagina" infoText="Deel de huidige pagina." />
        <div className="bottom-buttons">
          {/* <SearchButton /> */}
          <GoHomeButton />
          <BookmarkButton />
          <ShareButton customUrl="https://teerkost.nl/#/bewaard" buttonText="deel pagina" infoText="Deel de huidige pagina."/>
        </div>
        <div className="no-offers">
          <div className='notify-wrap'>
            Geen bewaarde aanbiedingen gevonden
          </div>
        </div>
      </div>
    )
}

export default NoBookmarks;
