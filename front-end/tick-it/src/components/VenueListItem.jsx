import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

export default function VenueListItem (props) {
    // const [location, setLocation] = useState([])

    // const getLocation = async () => {
    //     let response = await axios.get('http://127.0.0.1:8000/locations/')
    //     setLocation(response.data)
    //     console.log(response.data)
    // }

    // useEffect(() => {
    //     try {
    //         getLocation
    //     } catch (error) {
    //         console.error('Error fetching meal:', error)
    //     }
        
    // }, [])

    return (
        <div className='venueListItemContainer'>
                <h3>{props.venue.name}</h3>
                <h4>{props.venue.location}</h4>
                <h4>{location}</h4>
        </div>
       
       
    )
}