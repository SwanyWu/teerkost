import ShareDialog from "../components/ShareDialog";
import GoHomeButton from "../GoHomeButton";
import BookmarkButton from "../BookmarkButton";
import ShareButton from "../ShareButton";
import SearchButton from "../SearchButton";

function NotFound() {
    return (
      <div className="app-wrap">
        <a className="title-sober" href='https://teerkost.nl'><span>Teerkost</span></a>
        <ShareDialog customUrl="https://teerkost.nl/#/bewaard" buttonText="deel pagina" infoText="Deel de huidige pagina." />
        <div className="bottom-buttons">
          <GoHomeButton />
          <SearchButton />
          <BookmarkButton />
          <ShareButton customUrl="https://teerkost.nl/#/bewaard" buttonText="deel" infoText="Deel de huidige pagina."/>
        </div>
        <div className="not-found">
          <div className="notify-wrap">
            Deze link bestaat niet
          </div>
          <div className='notify-explainer'>
              Heb je een typfout gemaakt?
            </div>
        </div>
      </div>
    )
}

export default NotFound;
