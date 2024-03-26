import {useEffect, useState} from 'react'

const url = 'http://localhost:8000'

export default function VenueList() {

    const [data, setData] = useState([])
    const [searchText, setSearchText] = useState('')

    useEffect(() => {
        fetchData()
    },[searchText])

    const fetchData = async() => {
        const endpoint = `${url}/venues?venues=${searchText}`

        try {
            const response = await fetch(endpoint, {
                method: 'GET'
            })
            const data = await response.json()
            console.log(data)
            setData(data)
        }
        catch (e) {
            console.log(e)
        }
    }

    return (
        <div className='app'>
            <input type='search' placeholder='search' value={searchText} onChange={e=> setSearchText(e.target.value)}/>
            <ul>
                {data && data.map(el => <li key={el.id}>{el.name}</li>)}
            </ul>
            
        </div>
    )
}