import { useEffect } from "react";
import { MapContainer, TileLayer, Marker, useMap } from "react-leaflet";
import L from "leaflet";

// Import Leaflet CSS
import "leaflet/dist/leaflet.css";

// Fix for default markers in react-leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png",
  iconUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png",
  shadowUrl:
    "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png",
});

const ChangeView = ({ coords }) => {
  const map = useMap();

  useEffect(() => {
    if (coords && coords.length === 2) {
      console.log("Changing map view to:", coords);
      map.setView(coords, 15);
    }
  }, [coords, map]);

  return null;
};

const MapComponent = ({ coordinates, setCoordinates }) => {
  console.log("MapComponent received coordinates:", coordinates);

  return (
    <div style={{ height: "400px", marginTop: "20px" }}>
      <MapContainer
        center={coordinates || [20.5937, 78.9629]} // Default center (India)
        zoom={coordinates ? 15 : 4}
        scrollWheelZoom={true}
        style={{ height: "100%", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution="&copy; OpenStreetMap contributors"
        />
        {coordinates && (
          <>
            <ChangeView coords={coordinates} />
            <Marker
              position={coordinates}
              draggable={true}
              eventHandlers={{
                dragend: (e) => {
                  const { lat, lng } = e.target.getLatLng();
                  console.log("Dragged to:", lat, lng);
                  setCoordinates([lat, lng]); // Add this line
                },
              }}
            />
          </>
        )}
      </MapContainer>
    </div>
  );
};

export default MapComponent;
