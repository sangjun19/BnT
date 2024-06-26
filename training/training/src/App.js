import { useState } from 'react';

function FilterableProductTable() {
  const [products, setProducts] = useState([
    {category: "Fruits", price: "$1", stocked: true, name: "Apple"},
    {category: "Fruits", price: "$1", stocked: true, name: "Dragon Fruit"},
    {category: "Fruits", price: "$2", stocked: false, name: "Passion Fruit"},
    {category: "Vegetables", price: "$2", stocked: true, name: "Spinach"},
    {category: "Vegetables", price: "$4", stocked: false, name: "Pumpkin"},
    {category: "Vegetables", price: "$1", stocked: true, name: "Peas"}
  ]);
  const [filterText, setFilterText] = useState('');
  const [inStockOnly, setInStockOnly] = useState(false);

  return (
    <div>
      <Regist 
        PRODUCTS={products}
        setProducts={setProducts}
      />
      <SearchBar
        filterText={filterText}
        inStockOnly={inStockOnly}
        onFilterTextChange={setFilterText}
        onInStockOnlyChange={setInStockOnly} />
      <ProductTable
        products={products}
        filterText={filterText}
        inStockOnly={inStockOnly} />
    </div>
  );
}

function ProductCategoryRow({ category }) {
  return (
    <tr>
      <th colSpan="2">
        {category}
      </th>
    </tr>
  )
}

function ProductRow({ product }) {
  const name = product.stocked ? product.name : 
    <span style={{ color: 'red' }}>
      {product.name}
    </span>

    return (
      <tr>
        <td>{name}</td>
        <td>{product.price}</td>
      </tr>
    );
}

function ProductTable({ products, filterText, inStockOnly }) {
  const rows = [];
  let lastCategory = null;
  
  products.sort((a, b) => {
    if (a.category < b.category) {
      return -1;
    }
    if (a.category > b.category) {
      return 1;
    }

    if (a.name < b.name) {
      return -1;
    }
    if (a.name > b.name) {
      return 1;
    }
  })

  products.forEach((product) => {
    if (
      product.name.toLowerCase().indexOf(
        filterText.toLowerCase()
      ) === -1
    ) {
      return;
    }
    if (inStockOnly && !product.stocked) {
      return;
    }
    if (product.category !== lastCategory) {
      rows.push(
        <ProductCategoryRow
          category={product.category}
          key={product.category} />
      );
    }
    rows.push(
      <ProductRow
        product={product}
        key={product.name} />
    );
    lastCategory = product.category;
  });
    
    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    );
}

function Regist({ PRODUCTS, setProducts }) {

  const[kindValue, setKind] = useState('Fruits');
  const[nameValue, setName] = useState('');
  const[priceValue, setPrice] = useState('');

  const SelectBox = () => {
    return (
      <select value={kindValue} onChange={saveKind}>
        <option key="Fruits" value="Fruits">Fruits</option>
        <option key="Vegetables" value="Vegetables">Vegetables</option>
    </select>
    )
  }

  function activeRegist() {
    console.log(kindValue, nameValue, priceValue);
    const existingProduct = PRODUCTS.find(product => product.name === nameValue);
    if (existingProduct) {
      alert('Product already exists');
      return;
    }
    const newProduct = {category: kindValue, price: '$'+priceValue, stocked: true, name: nameValue};
    setProducts([...PRODUCTS, newProduct]);
    setKind('Fruits');
    setName('');
    setPrice('');
  }

  const saveKind = event => {
    setKind(event.target.value);
  }

  const saveName = event => {
    setName(event.target.value);
  }

  const savePrice = event => {
    setPrice(event.target.value);
  }

  return (
    <table>
      <thead>
        <tr>
          <th className="regist">
            <SelectBox/>
            <input type="text" placeholder="Name" value={nameValue} onChange={saveName}/>
            <input type="text" placeholder="Price" value={priceValue} onChange={savePrice}/>
            <button type="submit" onClick={activeRegist}>Regist</button>
          </th>
        </tr>
      </thead>
    </table>
  )
}

function SearchBar({ filterText, inStockOnly, onFilterTextChange, onInStockOnlyChange }) {
  return (
    <form>
      <input
      type="text"
      value={filterText}
      placeholder="Search..."
      onChange={(e) => onFilterTextChange(e.target.value)}
      />
      <label>
        <input
          type="checkbox"
          checked={inStockOnly}
          onChange={(e) => onInStockOnlyChange(e.target.checked)}
          />
        {' '}
        Only show products in stock
      </label>
    </form>
  );
}

export default function App() {
  return <FilterableProductTable products />;
}