import type { CategoryResp } from "../client";
import CategoryBadge from "./CategoryBadge";

const CategoryList = ({ categories }: { categories: CategoryResp[] }) => {
  return (
    <div className="flex mt-6 gap-2">
      {categories.map((category) => (
        <CategoryBadge key={category.id} name={category.name} />
      ))}
    </div>
  );
};

export default CategoryList;
