import { useNavigate } from 'react-router-dom'

export default function VenueListItem(props) {
    const navigate = useNavigate()

    const handleVenueClick = () => {
        navigate(`/venues/${props.venue.id}/events`)
    }

    return (
        <div className='eventListItemContainer' onClick={handleVenueClick} 
            style={{backgroundImage: `linear-gradient(rgba(0,0,0,0.0), rgba(0,0,0,0.7)), url(${props.venue.venue_img})`}}
        >
            <h3>{props.venue.name}</h3>
            <h4>{props.venue.city}, {props.venue.state}</h4>
        </div>
    )
}