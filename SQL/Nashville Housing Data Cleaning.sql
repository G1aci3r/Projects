
/*

Cleaning Data in SQL Queries

*/

select *
from [Nashville Housing].[dbo].[NashvilleHousing]
order by UniqueID


 --------------------------------------------------------------------------------------------------------------------------

-- Populate Property Address data

select *
from [Nashville Housing].[dbo].[NashvilleHousing]
--where PropertyAddress is null
order by ParcelID


select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, isnull(a.propertyaddress, b.PropertyAddress)
from [Nashville Housing].[dbo].[NashvilleHousing] as A
join [Nashville Housing].[dbo].[NashvilleHousing] as B
	on a.ParcelID = b.ParcelID
	and a.UniqueID != b.UniqueID
where a.PropertyAddress is null

update a 
set PropertyAddress = isnull(a.propertyaddress, b.PropertyAddress)
from [Nashville Housing].[dbo].[NashvilleHousing] as A
join [Nashville Housing].[dbo].[NashvilleHousing] as B
	on a.ParcelID = b.ParcelID
	and a.UniqueID != b.UniqueID
where a.PropertyAddress is null




--------------------------------------------------------------------------------------------------------------------------

-- Breaking out Address into Individual Columns (Address, City, State)

select PropertyAddress
from [Nashville Housing].[dbo].[NashvilleHousing]
--where PropertyAddress is null
--order by ParcelID

Select 
substring(PropertyAddress, 1, CHARINDEX(',',PropertyAddress)-1) as Address,
substring(PropertyAddress, CHARINDEX(',',PropertyAddress)+1, len(PropertyAddress)) as Address

from [Nashville Housing].[dbo].[NashvilleHousing]


Alter Table [Nashville Housing].[dbo].[NashvilleHousing]
add PropertySplitAddress Nvarchar(255);

Update [Nashville Housing].[dbo].[NashvilleHousing]
Set PropertySplitAddress = substring(PropertyAddress, 1, CHARINDEX(',',PropertyAddress)-1)




Alter Table [Nashville Housing].[dbo].[NashvilleHousing]
add PropertySplitCity nvarchar(225);

Update [Nashville Housing].[dbo].[NashvilleHousing]
Set PropertySplitCity = substring(PropertyAddress, CHARINDEX(',',PropertyAddress)+1, len(PropertyAddress))





SELECT *
FROM [Nashville Housing].[dbo].[NashvilleHousing]



select [OwnerAddress]
from [Nashville Housing].[dbo].[NashvilleHousing]


select
parsename(replace([OwnerAddress],',','.') ,3),
parsename(replace([OwnerAddress],',','.') ,2),
parsename(replace([OwnerAddress],',','.') ,1)
from [Nashville Housing].[dbo].[NashvilleHousing]


Alter Table [Nashville Housing].[dbo].[NashvilleHousing]
add OwnerSplitAddress Nvarchar(255);

Alter Table [Nashville Housing].[dbo].[NashvilleHousing]
add OwnerSplitCity Nvarchar(255);

Alter Table [Nashville Housing].[dbo].[NashvilleHousing]
add OwnerSplitState Nvarchar(255);


Update [Nashville Housing].[dbo].[NashvilleHousing]
Set OwnerSplitAddress = parsename(replace([OwnerAddress],',','.') ,3)

Update [Nashville Housing].[dbo].[NashvilleHousing]
Set OwnerSplitCity = parsename(replace([OwnerAddress],',','.') ,2)

Update [Nashville Housing].[dbo].[NashvilleHousing]
Set OwnerSplitState = parsename(replace([OwnerAddress],',','.') ,1)




--------------------------------------------------------------------------------------------------------------------------


-- Change Y and N to Yes and No in "Sold as Vacant" field

Select Distinct([SoldAsVacant]), Count([SoldAsVacant])
From [Nashville Housing].[dbo].[NashvilleHousing]
Group by [SoldAsVacant]
Order by 2


Select [SoldAsVacant], 
	Case when [SoldAsVacant] = 1 then 'Yes'
		 when [SoldAsVacant] = 0 then 'No'
	Else 'Unkonwn'
	END
From [Nashville Housing].[dbo].[NashvilleHousing]


Update [Nashville Housing].[dbo].[NashvilleHousing]
Set [SoldAsVacant] = 
	Case when [SoldAsVacant] = 1 then 'Yes'
		 when [SoldAsVacant] = 0 then 'No'
	Else [SoldAsVacant]
	END





-----------------------------------------------------------------------------------------------------------------------------------------------------------

-- Remove Duplicates

With Row_numCTE As(
Select *,
	ROW_NUMBER() Over(
	Partition by [ParcelID],
				 [PropertyAddress], 
				 [SalePrice], 
				 [SaleDate], 
				 [LegalReference]
				 Order by [UniqueID]
				 )row_num

From [Nashville Housing].[dbo].[NashvilleHousing]
--Order by [ParcelID]
)

--Delete
Select *
From Row_numCTE
--Where row_num > 1


---------------------------------------------------------------------------------------------------------

-- Delete Unused Columns

select *
from [Nashville Housing].[dbo].[NashvilleHousing]

Alter Table [Nashville Housing].[dbo].[NashvilleHousing]
Drop Column [OwnerAddress],
			[TaxDistrict],
			[PropertyAddress]








