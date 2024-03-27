import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

export default function VenueListItem (props) {
    const [location, setLocation] = useState([])

    useEffect(() => {
        try {
            const response = axios.get(`localhost:8000/locations`)
            console.log(response)
            setLocation(response)
            console.log(location)
        } catch (error) {
            console.error('Error fetching meal:', error)
        }
        
    }, [])

    return (
        <div>
        <ul>
            {props.venues.map(venue => (
                <div className='venueListItemContainer'>
                <h3>{venue.name}</h3>
                <h4>{venue.location}</h4>
                </div>
            ))}
        </ul>
        </div>
    )
}