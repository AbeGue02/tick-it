import { useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate, useParams } from 'react-router-dom'

export default function VenueListItem (props) {
    
    return (
        <div className='venueListItemContainer'>
                <h3>{props.venue.name}</h3>
                <h4>{props.venue.location}</h4>
        </div>
       
       
    )
}