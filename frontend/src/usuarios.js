import React, { useEffect, useState } from 'react';

function Usuarios() {
    const [usuarios, setUsuarios] = useState([]);
    const [nombre, setNombre] = useState('');
    const [email, setEmail] = useState('');
    const [privilegios, setPrivilegios] = useState('');
    const [horas, setHoras] = useState('');  // Agregar horas
    const [usuarioId, setUsuarioId] = useState(null);  // Guarda el ID del usuario que se está editando

    useEffect(() => {
        fetchUsuarios();
    }, []);

    // Función para obtener usuarios
    const fetchUsuarios = () => {
        fetch('http://localhost:8000/api/usuarios/')
            .then(response => response.json())
            .then(data => setUsuarios(data))
            .catch(error => console.error('Error al obtener los datos:', error));
    };

    // Función para agregar o editar un usuario
    const manejarUsuario = () => {
        const nuevoUsuario = { nombre, email, privilegios };
        const metodo = usuarioId ? 'PUT' : 'POST';  // Usar PUT si estamos editando, de lo contrario POST
        const url = usuarioId 
            ? `http://localhost:8000/api/usuarios/${usuarioId}/` 
            : 'http://localhost:8000/api/usuarios/';
        
        fetch(url, {
            method: metodo,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(nuevoUsuario),
        })
        .then(() => {
            fetchUsuarios(); // Refresca la lista después de agregar o editar
            setNombre(''); // Limpia el formulario
            setEmail('');
            setPrivilegios('');
            setUsuarioId(null);  // Reiniciar el ID después de editar
        })
        .catch(error => console.error('Error al procesar el usuario:', error));
    };

    // Función para eliminar un usuario
    const eliminarUsuario = (id) => {
        fetch(`http://localhost:8000/api/usuarios/${id}/`, {
            method: 'DELETE',
        })
        .then(() => {
            fetchUsuarios(); // Refresca la lista después de eliminar
        })
        .catch(error => console.error('Error al eliminar el usuario:', error));
    };

    // Función para seleccionar un usuario y llenar el formulario
    const seleccionarUsuario = (usuario) => {
        setNombre(usuario.nombre);
        setEmail(usuario.email);
        setPrivilegios(usuario.privilegios);
        setUsuarioId(usuario.id);  // Establece el ID del usuario que se está editando
    };

    // Función para agregar horas a un usuario
    const agregarHoras = (usuarioId) => {
        const horasData = { usuario: usuarioId, horas: parseInt(horas) };

        fetch(`http://localhost:8000/api/agregar_horas/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(horasData),
        })
        .then(() => {
            fetchUsuarios(); // Refresca la lista después de agregar horas
            setHoras(''); // Limpia el campo de horas
        })
        .catch(error => console.error('Error al agregar horas:', error));
    };

    return (
        <div className="container">
            <h1 className="my-4">Lista de Usuarios</h1>
            
            {/* Formulario para agregar o editar un usuario */}
            <div className="mb-4">
                <h2>{usuarioId ? 'Editar Usuario' : 'Agregar Usuario'}</h2>
                <div className="form-group">
                    <input
                        type="text"
                        className="form-control mb-2"
                        placeholder="Nombre"
                        value={nombre}
                        onChange={(e) => setNombre(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <input
                        type="email"
                        className="form-control mb-2"
                        placeholder="Email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <input
                        type="text"
                        className="form-control mb-2"
                        placeholder="Privilegios"
                        value={privilegios}
                        onChange={(e) => setPrivilegios(e.target.value)}
                    />
                </div>
                <button className="btn btn-primary" onClick={manejarUsuario}>
                    {usuarioId ? 'Guardar Cambios' : 'Agregar Usuario'}
                </button>
            </div>
    
            {/* Tabla que muestra los usuarios */}
            <table className="table table-striped">
                <thead className="thead-dark">
                    <tr>
                        <th>Nombre</th>
                        <th>Email</th>
                        <th>Privilegios</th>
                        <th>Horas</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {usuarios.map(usuario => (
                        <tr key={usuario.id}>
                            <td>{usuario.nombre}</td>
                            <td>{usuario.email}</td>
                            <td>{usuario.privilegios}</td>
                            <td>
                                <input
                                    type="number"
                                    className="form-control mb-2"
                                    placeholder="Horas"
                                    value={horas}
                                    onChange={(e) => setHoras(e.target.value)}
                                />
                                <button 
                                    className="btn btn-success btn-sm" 
                                    onClick={() => agregarHoras(usuario.id)}
                                >
                                    Agregar Horas
                                </button>
                            </td>
                            <td>
                                <button 
                                    className="btn btn-warning btn-sm me-2" 
                                    onClick={() => seleccionarUsuario(usuario)}
                                >
                                    Editar
                                </button>
                                <button 
                                    className="btn btn-danger btn-sm" 
                                    onClick={() => eliminarUsuario(usuario.id)}
                                >
                                    Eliminar
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Usuarios;
